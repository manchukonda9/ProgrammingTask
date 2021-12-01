import unittest
import logging
import imagedownloader
import os

class TestDownloader(unittest.TestCase):
     

	def test_input_file_validation(self):
		self.assertEqual( imagedownloader.check_permissions("image-links.txt",os.R_OK) , 0)
		self.assertIn( imagedownloader.check_permissions("not_available.txt",os.R_OK) , [73,77,66])

	def test_destination_folder_validation(self):
		self.assertEqual( imagedownloader.check_permissions("Downloaded-Images",os.W_OK) , 0)
		self.assertIn( imagedownloader.check_permissions("Images-NotAvailable",os.W_OK) , [73,77,66])

	def test_url_validation(self):
		self.assertTrue( imagedownloader.is_valid_url("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg") )
		self.assertTrue( imagedownloader.is_valid_url("https://store.google.com/US?utm_source=hp_header&utm_medium=google_ooo&utm_campaign=GS100042&hl=en-US") )
		self.assertFalse( imagedownloader.is_valid_url("I am not an URL") )

	def test_download_image_from_url(self):
		self.assertTrue( imagedownloader.download_image_from_url("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg", "Downloaded-Images") )
		self.assertTrue( imagedownloader.download_image_from_url("https://imagizer.imageshack.com/img922/8707/3q57kb.png", "Downloaded-Images") )
		self.assertFalse( imagedownloader.download_image_from_url("http://www.codingforums.com", "Downloaded-Images12") )

	def test_image_type_validation(self):
		self.assertTrue( imagedownloader.isImageType("image/png") )
		self.assertTrue( imagedownloader.isImageType("image/jpeg") )
		self.assertFalse( imagedownloader.isImageType("audio/mpeg") )
		self.assertFalse( imagedownloader.isImageType("application/json") )

	def test_check_folder_validation(self):
		self.assertEqual ( imagedownloader.check_folder("Downloaded-Images"), os.path.join(os.path.dirname(os.path.abspath(__file__)),"Downloaded-Images") )
		self.assertEqual ( imagedownloader.check_folder("TestingFolder"), os.path.join(os.path.dirname(os.path.abspath(__file__)),"TestingFolder") )

	def test_downlaod_images_from_file(self):
		self.assertEqual ( imagedownloader.download_images_from_file( "image-links.txt", "Images") , 0 )
		self.assertEqual ( imagedownloader.download_images_from_file( "image-links.txt", "Downloaded-Images") , 4 )
		self.assertEqual ( imagedownloader.download_images_from_file( "image-links2.txt", "Downloaded-Images") , 5 )

if __name__ == '__main__':
    unittest.main()
    logger = logging.getLogger(__name__)
    logging.basicConfig(format = '%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level = logging.INFO) 