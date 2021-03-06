# ProgrammingTask
## Blue Yonder coding task

### 1. Coding Task

As a step of the Blue Yonder hiring process, we kindly ask applicants to hand in a solution to the small programming task below. For us, this includes appropriate unit tests and the application of clean code principles. We value both technical correctness and coding style. Please be assured that there is no time limit, so you are free to tackle this task whenever it suits you best.

 

Given a plaintext file containing URLs, one per line, e.g.:

http://mywebserver.com/images/271947.jpg

http://mywebserver.com/images/24174.jpg

http://somewebsrv.com/img/992147.jpg

Write a script that takes this plaintext file as an argument and downloads all images, storing them on the local hard disk. Approach the problem as you would any task in a normal day’s work. Imagine this code will be used in important live systems, modified later on by other developers, and so on. 

You can choose any programming language you like (e.g Java, Python, or C++). We would like to receive your code via GitHub or a similar service.

### 2 Development stack used


* IDE: Visual Studio Code
* Operating System: MacOS Big Sur
* Python virtual environment
* Unittests
* Dependency Management: PIP

### 3 Python libraries 
        + logging
        + sys
        + urllib 
        + os 
        + errno
        + requests
        + unittest
        
### Requirements

All requirements for this functionality are listed in requirements.txt. To install
```
$ python3 -m pip install -r requirements.txt
```

### Implementation
```
$ python3 imagedownloader.py image-links.txt
```
Pass the plain text file containing image urls as an arguement to imagedownloader.py file. (image-links.txt contains image urls)

#### Output
```
4 Images Downloaded
```
Output for the code prints number of images successfully downloaded.

### Testing
```
$ python3 unit_testing.py
```
This file contains few testcases to validate the imagedownloader.py functionalities


