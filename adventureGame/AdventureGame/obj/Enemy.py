"""
@author: Reece Draper
"""

from obj import Weapon as WeaponClass

debug = False

class Enemy:
    
    # Summary:
    # Constructor - Creates an instance of the class.
    
    # Parameters
    # str _name - The name of the enemy.
    # int _level - The level of the enemy.
    # int _healthPoints - The amount of health the enemy has.
    # bool _isAlive - Whether the enemy is alive or not.
    # obj _equippedWeapon - The weapon that the enemy has equipped.
    def __init__(self, _name, _level, _healthPoints, _isAlive, _equippedWeapon):
        
        self.setName(_name)
        self.setLevel(_level)
        self.setHealthPoints(_healthPoints)
        self.setIsAlive(_isAlive)
        self.setEquippedWeapon(_equippedWeapon)
        
        if debug == True:
            print("\nConstructing Enemy...\n")
            print("Name: " + self.name)
            print("Level: " + self.level)
            print("Health Points: " + self.healthPoints)
            print("is Alive: " + self.isAlive)
            print("Equipped Weapon:" + self.equippedWeapon)
           
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