"""
@author: Reece Draper
"""

# Using utf-8 Character Encoding
# -*- coding: utf-8 -*-

from obj import Inventory as InventoryClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass

debug = False

# Summary:
# Class for playable character.
class Character:

    # Summary:
    # Constructor for Character Object.
    
    # Parameters:
    # str _name - The name of the playable character.
    # int _level - The skill level of the playable character.
    # int _healthPoints - The total amount of healthPoints the playable character has.
    # int _manaPoints - The total amount of mana points (Magical points) the playable character has.
    # int _experience - The total amount of experience the player has. Should directly tie to skill level.
    # int _defence - The total amount of defence the playable character has.
    # obj InventoryClass _inventory - The inventory of the playable character.
    # obj WeaponClass _equippedWeapon - The equipped weapon of the playable character.
    # obj ArmourSetClass _armourSet - The armour set the playable character has equipped.
    # int _gold - The amount of gold the character has.
    def __init__(self, _name, _level, _healthPoints, _manaPoints, _experience, _defence, _inventory, _equippedWeapon, _armourSet, _gold):

        # Setup attributes
        self.setName(_name)
        self.setLevel(_level)
        self.setHealthPoints(_healthPoints)
        self.setManaPoints(_manaPoints)
        self.setExperience(_experience)
        self.setDefence(_defence)
        self.setInventory(_inventory)
        self.setEquippedWeapon(_equippedWeapon)
        self.setArmourSet(_armourSet)
        self.setGold(_gold)
            
        # If in debug mode, print values to coonsole
        if debug == True:
            print("\nConstructing character...\n")
            print("Name: " + self.name)
            print("Level: " + str(self.level))
            print("Health Points: " + str(self.healthPoints))
            print("Mana Points: " + str(self.manaPoints))
            print("Experience: " + str(self.experience))
            print("Defence: " + str(self.defence))
            print("Inventory: " + str(self.inventory))
            print("Equipped Weapon: " + str(self.equippedWeapon))
            print("Armour Set: " + str(self.armourSet)) 
        
    # Summary:
    # Set the value of name.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Character name expected a string. Received: " + str(type(_name)) + " Check the type")
        
    # Summary:
    # Set the level of the playable character. Should directly correlate with experience points.
    def setLevel(self, _level):
        if type(_level) is int:
            self.level = _level
        else:
            raise TypeError("Character level expected an int. Received: " + str(type(_level)) + " Check the type")
        
    # Summary:
    # Set the total amount of health points for the playable character.
    def setHealthPoints(self, _healthPoints):
        if type(_healthPoints) is int:
            self.healthPoints = _healthPoints
        else:
            raise TypeError("Character health points expected an int. Received: " + str(type(_healthPoints)) + " Check the type")
  
    # Summary:
    # Set the total amount of mana (magical) points for the playable character.      
    def setManaPoints(self, _manaPoints):
        if type(_manaPoints) is int:
            self.manaPoints = _manaPoints
        else:
            raise TypeError("Character mana points expected an int. Received: " + str(type(_manaPoints)) + " Check the type")
    
    # Summary:
    # Set the total amount of experience points. Should directly relate to level.
    def setExperience(self, _experience):
        if type(_experience) is int:
            self.experience = _experience
        else:
            raise TypeError("Character experience expected an int. Received: " + str(type(_experience)) + " Check the type")
        
    # Summary:
    # Set the total amount of defence points for the playable character.
    def setDefence(self, _defence):
        if type(_defence) is int:
            self.defence = _defence
        else:
            raise TypeError("Character defence expected an int. Received: " + str(type(_defence)) + " Check the type")
    
    # For the next 3 methods, typecheck is not performed as type doesn't exist yet.
    # Summary:
    # Set the inventory of the playable character.
    def setInventory(self, _inventory):
        if isinstance(_inventory, InventoryClass.Inventory):
            self.inventory = _inventory
        else:
            raise TypeError("Character inventory expected an obj of type Inventory. Received: " + str(type(_inventory)) + " Check the type")
        
    # Summary:
    # Set the equipped weapon of the playable character.
    def setEquippedWeapon(self, _equippedWeapon):
        if isinstance(_equippedWeapon, WeaponClass.Weapon):
            self.equippedWeapon = _equippedWeapon
        else:
            raise TypeError("Character equippedWeapon expected an obj of type Weapon. Received: " + str(type(_equippedWeapon)) + " Check the type")
        
    # Summary:
    # Set the armour set of the character.
    def setArmourSet(self, _armourSet):
        if isinstance(_armourSet, ArmourSetClass.ArmourSet):
            self.armourSet = _armourSet
        else:
            raise TypeError("Character armourSet expected an obj of type ArmourSet. Received: " + str(type(_armourSet)) + " Check the type")
    
    # Summary:
    # Set the amount of gold of the character.
    def setGold(self, _gold):
        if type(_gold) is int:
            self.gold = _gold
        else:
            raise TypeError("Character gold expected an int. Received: " + str(type(_gold)) + " Check the type")