inventory = {
    'rope': 1, 
    'torch': 6, 
    'gold coin': 42, 
    'dagger': 1, 
    'arrow': 12
    }

def displayInventory(inventory):
    for keys in inventory.keys():
        print(inventory[keys], keys)
    
displayInventory(inventory)