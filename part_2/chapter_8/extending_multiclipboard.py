import shelve
import pyperclip
import sys

mcbShelve = shelve.open('mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelve[sys.argv[1]] = pyperclip.paste()
        print('Saved content to keyword')
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[1] in mcbShelve:
            del mcbShelve[sys.argv[1]]
        else:
            print("Keyword {sys.argv[1]} is not valid")
else:
    if sys.argv[1].lower() ==  'list':
        pyperclip.copy(str(list(mcbShelve.keys())))
        print('Copied all keyword in clipboard')
    elif sys.argv[1] in mcbShelve:
        pyperclip.copy(mcbShelve[sys.argv[1]])
        print("Content of clipboard is copied")
    elif sys.argv[1].lower() == 'delete':
        mcbShelve.clear()
        print('Deleted all items')

mcbShelve.close()
