"""
@author: Reece Draper
"""

from obj import Item as ItemClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass

debug = False

# Summary:
# Class for inventories of characters.
class Inventory:
    
    items = []
    
    # Summary:
    #   Constructor - Creates an instance of the class.
    # @Param:
    #   obj ItemClass list _items - A list of items for an inventory.
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
    
    # Summary:
    #   Sets the items of the Inventory.
    # @Param:
    #   obj ItemClass list _items - A list of items for an inventory.
    def setItems(self, _items = []):
        # Initilise list to contain items in inventory.        
        if len(_items) > 0 and len(_items) <= 10:
            for itemContents in _items:
                if isinstance(itemContents, ItemClass.Item) \
                or isinstance(itemContents, WeaponClass.Weapon) \
                or isinstance(itemContents, ArmourSetClass.ArmourSet):
                    self.items = _items
                else:
                    raise Exception("Inventory item expected an obj Item. Received: " + str(type(itemContents)) + " Check the type")
        elif len(_items) > 10:
            raise Exception("ERROR: Too many items for the inventory to initialise!")
        elif len(_items) <= 0:
            if debug == True:
                print("This inventory has been created without items!")
             
    # Summary:
    #   Adds an item to the inventory.
    def addItem(self, _item):
        if isinstance(_item, ItemClass.Item) \
        or isinstance(_item, WeaponClass.Weapon) \
        or isinstance(_item, ArmourSetClass.ArmourSet):
            if len(self.items) < 10:
                self.items.append(_item)
            else:
                print("Can't add " + _item.name + " to the inventory as it's full!")
        else:
            raise TypeError("Inventory item expected an obj Item. Received: " + str(type(_item)) + " Check the type")
            
    def dropItem(self, _item):
        raise Exception("Not implemented yet")
        
    # Summary:
    #   Discards the selected item.
    #   If the item inputted is of type obj Item, obj Weapon or obj ArmourSet search through the    
    #       list of items in the inventory via it's item name and then delete it.
    #   If the item is a string, search through via the name and then delete it.
    def discardItem(self, _item):
        if isinstance(_item, ItemClass.Item) \
        or isinstance(_item, WeaponClass.Weapon) \
        or isinstance(_item, ArmourSetClass.ArmourSet):
            for _itemInList in self.items:
                if _item.name == _itemInList.name:
                    try:
                        self.items.remove(_itemInList)
                        del _itemInList
                    except ValueError:
                        print("Failed to remove item in the list!")
                else:
                    print("Could not find item!")                
        elif type(_item) is str:
            for _itemInList in self.items:
                if _item == _itemInList.name:
                    try:
                        self.items.remove(_itemInList)
                        del _itemInList
                    except ValueError:
                        print("Failed to remove item in the list!")
                else:
                    print("Could not find item!")
        
    # Summary:
    #   Prints all the items in the inventory to the terminal.
    def printItems(self):
        print(str(self.items))
 