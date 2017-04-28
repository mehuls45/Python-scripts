#! python3
# PhoneNumber and Email

# TODO: Website Extractor

import pyperclip
import re

# phoneRegex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # area code
    (\s|-|\.)?                       # seperator
    (\d{3})                          # first 3 digits   
    (\s|-|\.)?                       # seperator
    (\d{4})                          # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
    )''',re.VERBOSE)


# emailRegex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # userName
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domainName
    (\.[a-zA-Z]{2,4})   # dot-something
    )''',re.VERBOSE)


# anotherPhoneRegex

anphoneRegex = re.compile(r'''(
    (\+\d{2})?       # Country code
    (\s|-|\.)?       # seperator
    (\d{3})          # 3 digits
    (\s|-|.|)?       # seperator
    (\d{3})          # 3 digits
    (\s|-|.|)?       # seperator
    (\d{4})          # 4 digits
    )''',re.VERBOSE)


# Find matches in clipboard text

text = str(pyperclip.paste())
matches = []

'''for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+groups[8]
    matches.append(phoneNum) '''

for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in anphoneRegex.findall(text):
    matches.append(groups[0])


    
# Copy results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
    
else:
    print('No numbers or email addresses were found')
    

