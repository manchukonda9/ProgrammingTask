
import logging
from urllib.parse import urlparse
import sys
import requests
import os
import errno


# Check whether URL is valid
def is_valid_url(url):
    parsed = urlparse(url.strip())

    if bool(parsed.netloc) and bool(parsed.scheme):
    	logging.info('Given url is a valid URL')
    	return True
    else:
    	logging.info('Given url is a invalid URL')
    	return False



#To check if a specific file has read or write permissions
def check_permissions(filename, permission):

    filepath = os.path.abspath(filename)

    result = 0
    logging.info("Checking file permission for file : %s",filepath)

    if permission == os.R_OK and not os.path.exists(filepath):
    	result = 66
    	logging.info('Status: %s - Not a valid path: %s\n',66,filename)
    elif permission == os.R_OK and not os.path.isfile(filepath):
    	result = 66
    	logging.info('Status: %s - Not a valid path: %s\n',66,filename)
    elif permission == os.R_OK and not os.access(filepath, permission):
    	result = 77
    	logging.info('Status: %s - No permission to read file: %s\n',77,filename)
    elif permission == os.W_OK and not os.path.exists(os.path.dirname(filepath)):
    	result = 73
    	logging.info('Status: %s - Not a valid path for output: %s\n',73,(os.path.dirname(filename)))
    elif permission == os.W_OK and not os.path.isdir(os.path.dirname(filepath)):
    	result = 73
    	logging.info('Status: %s - Not a directory: %s\n',73,(os.path.dirname(filename)))
    elif permission == os.W_OK and not os.path.isdir(filepath):
    	result = 73
    	logging.info('Status: %s - Not a valid directory: %s\n',73,filename)
    elif permission == os.W_OK and os.path.isdir(os.path.dirname(filepath)) and not os.access(filepath, permission):
    	result = 77
    	logging.info('Status: %s - No permission to write to directory: %s\n',77,(os.path.dirname(filename)))

    if result == 0:
    	logging.info(f'File is fine. Status : {result}')
    return result



# Check whether the content type is image
def isImageType(contentType):

    if 'image' in contentType.lower():
    	logging.info('Conent type is image')
    	return True
    else:
    	logging.info('Conent type is  not image')
    	return False



# Check or  new Create a destination folder 
def check_folder(folder_name):

	#Get folder permission status 
	status = check_permissions(folder_name, os.W_OK)
	if status == 0:
		folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),folder_name)
		logging.info('Destination folder path : %s',folder_path)
	
	elif status == 73:
		try:
			os.mkdir(folder_name)
			folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),folder_name)
		except Error as err:
			logging.error('Error while creating a new directory : %s',err)

	#Returning the path of the destination folder
	return folder_path


#To download image from given url to provided destination folder
def download_image_from_url(image_url, destination_folder):

	if not is_valid_url(image_url):
		return False

	destination_folder_status = check_permissions(destination_folder, os.W_OK)

	if(destination_folder_status != 0):
		return False

	filename = image_url.split("/")[-1]

	try:
		res = requests.get(image_url)

		if res.status_code == 200:
			# Checking if the response has image content type
			if isImageType(res.headers.get('content-type')):
				try:
					with open(f"{destination_folder}/{filename}", "wb+") as f:
						f.write(res.content)
						logging.info('Image downloaded successfully!')
						return True     
				except:
					logging.error('Error/Exception while writing response content to file')
		            

		else:
			logging.error('Error retrieving image')

	except Error as err:
		logging.error('Error when making GET request : %s',err)

	return False




#To save images retreived from url in given file to provided destination folder,  
def download_images_from_file(filepath, destination_folder):
   
	with open(filepath, "r") as f:
		file_urls = f.readlines()

	logging.info('Total lines in input file : %s',len(file_urls))

	count = 0

	if len(file_urls) > 0 :
		for i,input_url in enumerate(file_urls):
			logging.info('Line{}: Reading {}'.format(i+1, input_url))

			#Checking if the current line is a valid url
			if is_valid_url(input_url):

				is_downloaded = download_image_from_url(input_url.strip(),destination_folder)

				if(is_downloaded):
					count = count+1
	
	else: 
		logging.error('Input file is empty!!')

	print(f"{count} Images Downloaded.")
	return count




# MAIN FUNCTION START
def main(filepath):

	# setup logs
	logging.basicConfig(filename='image-downloader.log', level=logging.INFO, format='%(filename)s - %(asctime)s : %(message)s')


	#Check for input file permissions
	input_file_status = check_permissions(filepath, os.R_OK)

	if (input_file_status != 0):
		logging.error("Error in provided filepath")
		print("Error in provided filepath")
		return

	# Provide a destination folder name 
	destination_folder_name = "Downloaded-Images"

	# Check for destination folder
	destination_folder_path = check_folder(destination_folder_name)

	#Download images from given file, tp 
	images_downloaded = download_images_from_file(filepath,destination_folder_name)
 
	return images_downloaded

# CALL MAIN FUNCTION
if __name__ == '__main__':
    main(str(sys.argv[1]))
