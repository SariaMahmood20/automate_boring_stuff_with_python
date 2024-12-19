import re

text = "sjkdfs asdfhskdjfh sdfhskdjfhsjk jksdhfjkshdfkjlash"

subsitute = input("Enter the text")
mo = re.sub(subsitute, '', text)
print(mo)