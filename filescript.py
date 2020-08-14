#! /usr/bin/env python 3

import shutil,os,re,os.path

root_directory = os.chdir('/Users/vanessatay/Documents')
directory_files=os.listdir(root_directory)
#folderName=os.walk('Users/vanessatay/Documents')
fileRegex=re.compile(r'''Resume|test|Application|Template|Readings|Article|
Lecture|letter|interview|Spa|Terminal|
NTU|flowcontrolswordfish|PhoneandEmail
|Textbook|Admission|Lab|interview|.DS_Store''' , re.VERBOSE)
#mo=fileRegex.search('') #create regex object
#loop through the entire directory
for file in directory_files: 
        mo=fileRegex.search(file)
        filename=mo.group()
        #if matching object=name of folder that exists
        if os.path.exists(filename):
            shutil.move(file,filename)
        #add the file into the folder
        else:
            #Create new folder based on mo of regex search
            os.makedirs(filename)
            shutil.move(file,filename)
        


#if folder no exist,create new folder based on the matching object that returns
#add into file
#if folder exist, just add file into it
