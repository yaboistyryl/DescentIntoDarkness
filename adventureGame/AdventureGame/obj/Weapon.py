"""
@author: Reece Draper
"""

import random

debug = True

class Weapon:
    # Common, Uncommon, Rare, Ultra Rare, Legendary
    rarityMultiplier = [5, 10, 15, 20, 25]
    
    # Summary:
    # Constructor - Creates an instance of the class.  
    
    # Parameters:
    # str _name - The name of the weapon.
    # int _value - The value of the weapon.
    # int _damage - The amount of damage the weapon deals.
    # int _defence - The amount of defense the weapon provides when equipped.
    def __init__(self):
        
        self.generateRandomWeapon()
        
        if debug == True:
            print("\nConstructing Weapon...\n")
            print("Name: " + self.name)
            print("Value: " + str(self.value))
            print("Damage: " + str(self.damage))
            print("Defence: " + str(self.defence))
    
    # Summary:
    # Set the name of the weapon.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Weapon name expected a string. Received: " + str(type(_name)) + " Check the type")
    
    # Summary:
    # Set the value of the weapon.
    def setValue(self, _value):
        if type(_value) is int:
            self.value = _value
        else:
            raise TypeError("Weapon value expected an int. Received: " + str(type(_value)) + " Check the type")
        
    # Summary:
    # Set the damage of the weapon.
    def setDamage(self, _damage):
        if type(_damage) is int:
            self.damage = _damage
        else:
            raise TypeError("Weapon damage expected an int. Received: " + str(type(_damage)) + " Check the type")
        
    # Summary:
    # Set the defence of the weapon.
    def setDefence(self, _defence):
        if type(_defence) is int:
            self.defence = _defence
        else:
            raise TypeError("Weapon defence expected an int. Received: " + str(type(_defence)) + " Check the type")
    
    def generateRandomWeapon(self):
        # Generate rarity of weapon
        self.rarity = self.generateRandomWeaponRarity()
        
        self.setRandomName()
        self.setRandomValue()
        self.setRandomDamage()
        self.setRandomDefence()
    
    # Summary:
    #   Set a random name from a predefined list of names.      
    def setRandomName(self):#
        rarities = ["Common", "Uncommon", "Rare", "Ultra Rare", "Legendary"]
        namesList = ["Sword", "Long Sword", "Great Sword", "Daggers", "Karambit", "Knife", "Sickle", "Spear", "Scythe", "Mace"]
        
        randomNameIndex = random.randint(0, len(namesList) - 1)
        
        fullName = str(rarities[self.rarity]) + " " + str(namesList[randomNameIndex])
        
        self.setName(fullName)
    
    def setRandomValue(self):
        baseValue = random.randint(1, 100)
        
        self.setValue(baseValue * self.rarityMultiplier[self.rarity])
    
    def setRandomDamage(self):
        baseDamage = random.randint(1, 10)
        
        self.setDamage(baseDamage * self.rarityMultiplier[self.rarity])
    
    def setRandomDefence(self):
        baseDefence = random.randint(1, 10)
        
        self.setDefence(baseDefence * self.rarityMultiplier[self.rarity])
        
    # Summary:        
    #   Generate a random weapon rarity
    # Rarity List:
    #   Common - 35% chance
    #   Uncommon - 30% chance
    #   Rare - 20% chance
    #   Very Rare - 10% chance
    #   Legendary - 5% chance
    # return index - The random weapon rarity.
    @staticmethod
    def generateRandomWeaponRarity():
        
        # Generate random number between 0 and 100 return a rarity value off of it.
        randNumb = random.randint(0, 100)
        # Uncommon
        if randNumb <= 35:
            index = 0
        # Common
        elif randNumb <= 65:
            index = 1
        # Rare
        elif randNumb <= 85:
            index = 2
        # Ultra Rare
        elif randNumb <= 95:
            index = 3
        # Legendary
        elif randNumb <= 100:
            index = 4
        else:
            raise Exception("You are terrible at coding if we got here")
            
        return index
