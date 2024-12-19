import re

strongPassword = re.compile(r'''
 (?=.*[a-z]) #Atleast one lower case letter
 (?=.*[A-Z]) #Atleast one upper case letter
 (?=.*\d) #Atleast one digit
 (?=.*(%_\W)) #Atleast one special character
 {8,}
''', re.VERBOSE)

password = input("Enter a password: ")

if strongPassword.findall(password):
    print(password)
else:
    print("Weak Password")