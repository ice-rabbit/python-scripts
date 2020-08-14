#! /usr/bin/env python 3

import re, pyperclip

#TODO:Create a regex for phone numbers
phoneRegex=re.compile(r'''
((\d\d\d\d)\s(\d\d\d\d)) #phone number in 1234 5678 version
''', re.VERBOSE)

#Create a regex for email
emailRegex=re.compile(r'''
[a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]
''', re.VERBOSE)
#Get the text off the clipboard

text=pyperclip.paste()
#Extract the email/phone from the text
extractedPhone=phoneRegex.findall(text)
extractedEmail=emailRegex.findall(text)
print(extractedPhone)
print(extractedEmail)
#Copy the extracted email/phone to the clipboard
