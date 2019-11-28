"""
@author: Reece Draper
"""

from obj import Item as ItemClass

debug = False

# Summary:
# Class for inventories of characters.
class Inventory:
    
    # Summary:
    # Constructor - Creates an instance of the class.

    # Parameters:
    # obj ItemClass list _items - A list of items for an inventory.
    def __init__(self, _items = []):
        if debug == True:
            print("\nConstructing Inventory...\n")
        
        self.setItems(_items)
        
        if debug == True:
            print("Contents:\n")
            print("    Class Attribute Array:")
            for itemValue in self.items:
                print("    " + itemValue)
            print("    __init__ Paramter Array:")
            for itemValue2 in _items:
                print("    " + itemValue)
                
    def setItems(self, _items = []):
        # Initilise list to contain items in inventory.        
        if len(_items) > 0 and len(_items) <= 10:
            for itemContents in _items:
                if isinstance(itemContents, ItemClass.item):
                    self.items = _items
                else:
                    raise Exception("Inventory item expected an obj Item. Received: " + str(type(itemContents)) + " Check the type")
        elif len(_items) > 10:
            raise Exception("ERROR: Too many items for the inventory to initialise!")
        elif len(_items) <= 0:
            if debug == True:
                print("This inventory has been created without items!")
 