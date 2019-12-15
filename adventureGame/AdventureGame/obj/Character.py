"""
@author: Reece Draper
TO DO:
    LevelUp() Function.
"""

# Using utf-8 Character Encoding
# -*- coding: utf-8 -*-

from obj import Inventory as InventoryClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass
from obj import Enemy as EnemyClass

debug = False

# Summary:
# Class for character.
class Character:

    # Summary:
    #   Constructor for Character Object.
    # @Params:
    #   str _name - The name of the character.
    #   int _level - The skill level of the character.
    #   int _healthPoints - The total amount of healthPoints the character has.
    #   int _manaPoints - The total amount of mana points (Magical points) the character has.
    #   int _experience - The total amount of experience the player has. Should directly tie to skill level.
    #   int _defence - The total amount of defence the character has.
    #   obj InventoryClass _inventory - The inventory of the character.
    #   obj WeaponClass _equippedWeapon - The equipped weapon of the character.
    #   obj ArmourSetClass _armourSet - The armour set the character has equipped.
    #   int _gold - The amount of gold the character has.
    def __init__(self, _name):
        
        # Create random instance of weapon 
        equippedWeapon = WeaponClass.Weapon()
        # Generate starting weapon.
        equippedWeapon.generateStartingWeapon()
        
        # Setup attributes
        self.setName(_name)
        self.setLevel(1)
        self.setHealthPoints(50)
        self.setExperience(0)
        self.setDefence(0)
        self.setIsAlive(True)
        self.setInventory(InventoryClass.Inventory())
        self.setEquippedWeapon(equippedWeapon)
        self.setArmourSet(ArmourSetClass.ArmourSet("Basic Armour", 0, 10))
        self.setGold(50)
            
        # If in debug mode, print values to console
        if debug == True:
            print("\nConstructing character...\n")
            self.printCharacterInfo()
        
    # Summary:
    #   Sets the value of name.
    # @Param:
    #   string _name - The name of the character.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Character name expected a string. Received: " + str(type(_name)) + " Check the type")
        
    # Summary:
    #   Sets the level of the character. Should directly correlate with experience points.
    # @Param:
    #   int _level - The level of the character.
    def setLevel(self, _level):
        if type(_level) is int:
            self.level = _level
        else:
            raise TypeError("Character level expected an int. Received: " + str(type(_level)) + " Check the type")
        
    # Summary:
    #   Sets the total amount of health points for the character.
    # @Param:
    #   int _healthPoints - The amount of the health points for the character.
    def setHealthPoints(self, _healthPoints):
        if type(_healthPoints) is int:
            self.healthPoints = _healthPoints
        else:
            raise TypeError("Character health points expected an int. Received: " + str(type(_healthPoints)) + " Check the type")
        
        if _healthPoints <= 0:
            self.setIsAlive(False)
    
    def setIsAlive(self, _isAlive):
        if type(_isAlive) is bool:
            self.isAlive = _isAlive
        else:
            raise TypeError("Character alive status expected an bool. Received: " + str(type(_isAlive)) + " Check the type")
    
        if _isAlive == False:
            print(self.name + " has been killed by the monsters of darkness")
    
    # Summary:
    #   Sets the total amount of experience points. Should directly relate to level.
    # @Param:
    #   int _experience - The experience of the player.
    def setExperience(self, _experience):
        if type(_experience) is int:
            self.experience = _experience
        else:
            raise TypeError("Character experience expected an int. Received: " + str(type(_experience)) + " Check the type")
        
    # Summary:
    #   Sets the total amount of defence points for the character.
    # @Param:
    #   int _defence - The defence of the character.
    def setDefence(self, _defence):
        if type(_defence) is int:
            self.defence = _defence
        else:
            raise TypeError("Character defence expected an int. Received: " + str(type(_defence)) + " Check the type")

    # Summary:
    #   Sets the inventory of the character.
    # @Param:
    #   obj Inventory _inventory - The inventory of the character.
    def setInventory(self, _inventory):
        if isinstance(_inventory, InventoryClass.Inventory):
            self.inventory = _inventory
        else:
            raise TypeError("Character inventory expected an obj of type Inventory. Received: " + str(type(_inventory)) + " Check the type")
        
    # Summary:
    #   Sets the equipped weapon of the character.
    # @Param:
    #   obj Weapon _equippedWeapon - The weapon that the character is going to use to fight.
    def setEquippedWeapon(self, _equippedWeapon):
        if isinstance(_equippedWeapon, WeaponClass.Weapon):
            self.equippedWeapon = _equippedWeapon
        else:
            raise TypeError("Character equippedWeapon expected an obj of type Weapon. Received: " + str(type(_equippedWeapon)) + " Check the type")
        
    # Summary:
    #   Sets the armour set of the character.
    # @Param:
    #   obj ArmourSet _armourSet - The armour set that the character is going to wear.
    def setArmourSet(self, _armourSet):
        if isinstance(_armourSet, ArmourSetClass.ArmourSet):
            self.armourSet = _armourSet
        else:
            raise TypeError("Character armourSet expected an obj of type ArmourSet. Received: " + str(type(_armourSet)) + " Check the type")
    
    # Summary:
    #   Sets the amount of gold of the character.
    # @Param:
    #   The amount of gold the character has.
    def setGold(self, _gold):
        if type(_gold) is int:
            self.gold = _gold
        else:
            raise TypeError("Character gold expected an int. Received: " + str(type(_gold)) + " Check the type")
    
    def attack(self, _target):
        if isinstance(_target, EnemyClass.Enemy):
            print(self.name + " attacked " + _target.name + " for " + str(self.equippedWeapon.damage) + " damage!")
            _target.setHealthPoints(_target.healthPoints - self.equippedWeapon.damage)
        else:
            raise Exception("Target is not an enemy!")
    
    def openInventory(self):
        self.inventory.printItems()
    
    # Summary:
    #   Prints the the attributes of the character.
    def printCharacterInfo(self):
        print("\n")
        print("Name: " + self.name)
        print("Level: " + str(self.level))
        print("Health Points: " + str(self.healthPoints))
        print("Mana Points: " + str(self.manaPoints))
        print("Experience: " + str(self.experience))
        print("Defence: " + str(self.defence))
        print("Inventory: " + str(self.inventory))
        print("Equipped Weapon: " + str(self.equippedWeapon))
        print("Armour Set: " + str(self.armourSet))