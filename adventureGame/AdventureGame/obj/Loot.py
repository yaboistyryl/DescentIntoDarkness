"""
@author: Reece Draper
"""

from obj import Item as ItemClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass

# Summary:
# Class for loot
class Loot():
    
    # Summary:
    #   Constructor - Creates an instance of the class.  
    # @Param:
    #   obj ItemClass/obj WeaponClass/obj ArmourSetClass _item - The item that can be looted.
    #   int _gold - The amount of gold that can be looted.
    def __init__(self, _item, _gold):
        
        self.setItem(_item)
        self.setGold(_gold)
    
    # Summary:
    #   Sets the type of loot that will be received.
    # @Param:
    #   obj ItemClass/obj WeaponClass/obj ArmourSetClass _item - The item that can be looted.
    def setItem(self, _item):
        if isinstance(_item, ItemClass.Item) \
        or isinstance(_item, WeaponClass.Weapon) \
        or isinstance(_item, ArmourSetClass.ArmourSet):
            self.item = _item
        else:
            raise TypeError("Loot item expected an obj Item. Received: " + str(type(_item)) + " Check the type")
    
    # Summary:
    #   Sets the amount of gold that will be received.
    # @Param:
    #   int _gold - The amount of gold that can be looted.    
    def setGold(self, _gold):
        if type(_gold) is int:
            self.gold = _gold
        else:
            raise TypeError("Loot gold expected an int. Received: " + str(type(_gold)) + " Check the type")