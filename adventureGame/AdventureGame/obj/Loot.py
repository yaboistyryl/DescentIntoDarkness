"""
@author: Reece Draper
"""

from obj import Item as ItemClass

# Summary:
# Class for loot
class Loot():
    
    # Summary:
    # Constructor - Creates an instance of the class.  
    
    # Parameters:
    # obj ItemClass _item - The item that can be looted.
    # int _gold - The amount of gold that can be looted.
    def __init__(self, _item, _gold):
        
        self.setItem(_item)
        self.setGold(_gold)
            
    def setItem(self, _item):
        if isinstance(_item, ItemClass.item):
            self.item = _item
        else:
            raise TypeError("Loot item expected an obj Item. Received: " + str(type(_item)) + " Check the type")
            
    def setGold(self, _gold):
        if type(_gold) is int:
            self.gold = _gold
        else:
            raise TypeError("Loot gold expected an int. Received: " + str(type(_gold)) + " Check the type")