import pyperclip
import re

matches = []

# 897-1234-567
phone_pattern = re.compile(r'''
    (\d{3}|\(\d{3}\))?        # Optional area code
    (\s|-|\.)?                # Optional separator
    \d{3}                     # First 3 digits
    (\s|-|\.)                 # Separator
    \d{4}                     # Last 4 digits
''', re.VERBOSE)

# sariamahmood18@gmail.com
email_pattern = re.compile(r'''
    [a-zA-Z0-9._%-]+          # Username
    @
    [a-zA-Z0-9.-]+            # Domain name
    (\.[a-zA-Z]{2,4})         # Top-level domain
''', re.VERBOSE)

text = str(pyperclip.paste())

for groups in phone_pattern.findall(text):
    phoneNum = '-'.join([groups[1], groups[2], groups[2]])
    matches.append(phoneNum)

for groups in email_pattern.findall(text):
    email = ''.join(groups[0])
    matches.append(email)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print("Found nothing")
