"""
@author: Reece Draper

TO DO:
    Create a way to randomly generate.
"""

debug = False

# Summary:
# Class for items of inventories.
class Item:
    
    # Summary:
    #   Constructor - Creates an instance of the class.  
    # @Param:
    #   str _itemName - The name of the item.
    #   str _itemType - The type of item.
    #   int _itemUsesLeft - The amount of uses the item has left before it breaks.
    #   int _itemValue - The amount the item is worth.
    def __init__(self, _name, _type, _usesLeft, _value):
        
        self.setName(_name)
        self.setType(_type)
        self.setUsesLeft(_usesLeft)
        self.setValue(_value)
        
        if debug == True:
            print("\nConstructing item...\n")
            self.printItemInfo()

    # Summary:
    #   Sets the name of the item.
    # @Param:
    #   string _name - The name of the item.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Item name expected a string. Received: " + str(type(_name)) + " Check the type")
      
    # Summary:
    #   Sets the type of item.
    # @Param:
    #   string _type - The type of item.
    def setType(self, _type):
        if type(_type) is str:
            self.type = _type
        else:
            raise TypeError("Item type expected a string. Received: " + str(type(_type)) + " Check the type")
        
    # Summary:
    #   Set the amount of item uses left.
    # @Param:
    #   int _usesLeft - The amount of uses the item has left.
    def setUsesLeft(self, _usesLeft):
        if type(_usesLeft) is int:
            self.usesLeft = _usesLeft
        else:
            raise TypeError("Item usesLeft expected a int. Received: " + str(type(_usesLeft)) + " Check the type")
    
    # Summary:
    #   Set the value of the item.
    # @Param:
    #   int _value - The value of the item.
    def setValue(self, _value):
        if type(_value) is int:
            self.value = _value
        else:
            raise TypeError("Item value expected a int. Received: " + str(type(_value)) + " Check the type")
            
    # Summary:
    #   Print the attributes of the item instance.
    def printItemInfo(self):
        print("Name: " + self.name)
        print("Type: " + self.type)
        print("Uses left: " + str(self.itemUsesLeft))
        print("Value: " + str(self.Value))