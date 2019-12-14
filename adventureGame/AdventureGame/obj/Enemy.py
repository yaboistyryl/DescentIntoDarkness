"""
@author: Reece Draper
"""

from obj import Weapon as WeaponClass
import random

debug = True

class Enemy:
    
    # Summary:
    #   Constructor - Creates an instance of the class.
    # @Param:
    #   int _level - The level of the enemy.
    #   bool _isAlive - Whether the enemy is alive or not.
    def __init__(self, _level, _isAlive):
        
        self.setRandomName()
        self.setLevel(_level)
        self.setHealthPointsFromLevel()
        self.setIsAlive(_isAlive)
        self.setEquippedWeapon(WeaponClass.Weapon())
           
    # Summary:
    #   Sets the name of the enemy.
    # @Param:
    #   string _name - The name of the the enemy.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Enemy name expected a string. Received: " + str(type(_name)) + " Check the type.")
    
    # Summary:
    #   Sets the level of the enemy
    # @Param:
    #   int _level - The level of the enemy.
    def setLevel(self, _level):
        if type(_level) is int:
            self.level = _level
        else:
            raise TypeError("Enemy level expected a int. Received: " + str(type(_level)) + " Check the type.")
        
    # Summary:
    #   Sets the amount of health the enemy has.
    # @Param:
    #   int _healthPoints - The amount of health points the enemy has.
    def setHealthPoints(self, _healthPoints):
        
        if type(_healthPoints) is int:
            # Make enemy die if healthpoints get below 0
            if _healthPoints <= 0:
                self.setIsAlive(False)
            self.healthPoints = _healthPoints
        else:
            raise TypeError("Enemy healthPoints expected a int. Received: " + str(type(_healthPoints)) + " Check the type.")
    
    # Summary:
    #   Sets whether the enemy is alive or not.
    # @Param:
    #   bool _isAlive - Whether the enemy is alive or not.
    def setIsAlive(self, _isAlive):
        if type(_isAlive) is bool:
            self.isAlive = _isAlive
        else:
            raise TypeError("Enemy isAlive expected a bool. Received: " + str(type(_isAlive)) + " Check the type.")
        
        if self.isAlive == False:
            print("\n" + self.name + " has been slain!")
            
        
    # Summary:
    #   Sets the equipped weapon of the enemy
    # @Param:
    #   obj Weapon _equippedWeapon - The weapon that the enemy uses.
    def setEquippedWeapon(self, _equippedWeapon):
        if isinstance(_equippedWeapon, WeaponClass.Weapon):
            self.equippedWeapon = _equippedWeapon
        else:
            raise TypeError("Enemy equippedWeapon expected an obj of type Weapon. Received: " + str(type(_equippedWeapon)) + " Check the type.")
               
    # Summary:
    #   Generates a random name froma predefined list.
    def setRandomName(self):
        # Predefined list.
        nameList = ["Skeleton", "Zombie", "Goblin", "Dark Knight", "Kobold", "half orc", "orc", "hobgoblin", "ogre"]
        
        # Create random index number based on length of predefined list.
        randomEnemyNameIndex = random.randint(0, len(nameList)-1)
        
        # get random name from predefined list.
        self.setName(nameList[randomEnemyNameIndex])
    
    # Summary:
    #   Creates a random level +- 2 from player level to keep it balanced.
    # @Param:
    #   int _playerLevel - The level of the player.
    def setRandomLevel(self, _playerLevel):
        if _playerLevel - 2 <= 0:
            self.setLevel(1)
        elif _playerLevel + 2 >= 30:
            self.setLevel(30)
        else:
            self.setLevel(random.randint(_playerLevel - 2, _playerLevel + 2))
          
    # Summary:
    #   Sets the health points from the player's current level. Player Health Points = player level x 10. 
    def setHealthPointsFromLevel(self):
        self.setHealthPoints(self.level * 10)
    
    # Summary:
    #   Prints the attributes assigned to the instance of enemy.
    def printEnemyInfo(self):
        vowels = ('a','e','i','o','u')
        # Ensure that the string is outputted grammatically.
        if self.name.startswith(vowels):
            print("\nYou see an " + self.name + ". It looks to be level " + str(self.level) + ". It has " + str(self.healthPoints) + " health remaining!")
        else:
            print("\nYou see a " + self.name + ". It looks to be level " + str(self.level) + ". It has " + str(self.healthPoints) + " health remaining!")