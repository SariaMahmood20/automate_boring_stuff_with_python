dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
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
    
def addItems(inventory, loot):
    for item in loot:
        inventory[item]  = inventory.get(item, 0) + 1

addItems(inventory, dragonLoot)
displayInventory(inventory)