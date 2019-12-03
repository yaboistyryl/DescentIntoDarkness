"""
@author: Reece Draper
"""

from obj import Weapon as WeaponClass
import random

debug = True

class Enemy:
    
    # Summary:
    # Constructor - Creates an instance of the class.
    
    # Parameters
    # str _name - The name of the enemy.
    # int _level - The level of the enemy.
    # int _healthPoints - The amount of health the enemy has.
    # bool _isAlive - Whether the enemy is alive or not.
    # obj _equippedWeapon - The weapon that the enemy has equipped.
    def __init__(self, _level, _isAlive):
        
        self.setRandomName()
        self.setLevel(_level)
        self.setHealthPointsFromLevel()
        self.setIsAlive(_isAlive)
        self.setEquippedWeapon(WeaponClass.Weapon())
        
        if debug == True:
            print("\nConstructing Enemy...\n")
            print("Name: " + self.name)
            print("Level: " + str(self.level))
            print("Health Points: " + str(self.healthPoints))
            print("is Alive: " + str(self.isAlive))
           
    # Summary:
    # Set the name of the enemy.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Enemy name expected a string. Received: " + str(type(_name)) + " Check the type.")
    
    # Summary:
    # Set the level of the enemy
    def setLevel(self, _level):
        if type(_level) is int:
            self.level = _level
        else:
            raise TypeError("Enemy level expected a int. Received: " + str(type(_level)) + " Check the type.")
        
    # Summary:
    # Set the amount of health the enemy has.
    def setHealthPoints(self, _healthPoints):
        if type(_healthPoints) is int:
            self.healthPoints = _healthPoints
        else:
            raise TypeError("Enemy healthPoints expected a int. Received: " + str(type(_healthPoints)) + " Check the type.")
    
    # Summary:
    # Set whether the enemy is alive or not.
    def setIsAlive(self, _isAlive):
        if type(_isAlive) is bool:
            self.isAlive = _isAlive
        else:
            raise TypeError("Enemy isAlive expected a bool. Received: " + str(type(_isAlive)) + " Check the type.")
        
    # Summary:
    # Set the equipped weapon of the enemy
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
            
    def setHealthPointsFromLevel(self):
        self.setHealthPoints(self.level * 10)