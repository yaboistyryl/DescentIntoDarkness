# -*- coding: utf-8 -*-
"""
@author: Reece Draper
"""

from obj import Enemy as EnemyClass

debug = False

class dungeonRoom:
    # Summary:
    # Constructor - Creates an instance of the class.
    
    # Parameters:
    # str _name - the name of the dungeon room.
    # str _roomType - the type of dungeon room.
    # str _entryPoint - The entryPoint of the dungeon room.
    # str _flavourTest - The description of the dungeon room.
    # bool _hasVisited - Whether the player has visited or not.
    # bool _hasEnemies - Whether the room has enemies or not.
    # int _enemyNumber - The amount of enemies in the dungeon room.
    # bool _hasChest - Whether the room has a chest or not.
    def __init__(self, _name, _hasEnemies, _enemyList, _hasChest):

        self.setName(_name)
        self.setHasEnemies(_hasEnemies)
        self.setEnemyList(_enemyList)
        self.setHasChest(_hasChest)
        
        if debug == True:
            print("\nConstructing dungeonRoom...\n")
            print("Name: " + self.name)
            print("Has Enemies: " + self.hasEnemies)
            print("Enemy Number: " + str(self.enemyNumber))
            print("Has Chest: " + self.hasChest)
            
    # Summary:
    # Set the name of the dungeon room.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("DungeonRoom name expected a string. Received: " + str(type(_name)) + " Check the type")
        
    # Summary:
    # Set whether the room has enemies or not.
    def setHasEnemies(self, _hasEnemies):
        if type(_hasEnemies) is bool:
            self.hasEnemies = _hasEnemies
        else:
            raise TypeError("DungeonRoom hasEnemies expected a bool. Received: " + str(type(_hasEnemies)) + " Check the type")
    
    def setEnemyList(self, _enemyList):
        if type(_enemyList) is list:
            for enemyListContent in _enemyList:
                if isinstance(enemyListContent, EnemyClass.Enemy):
                    self.enemyList = _enemyList
        else:
            raise TypeError("DungeonRoom enemyList expected a list. Received: " + str(type(_enemyList)) + " Check the type")
    
    # Summary:
    # Set the amount of enemies in the dungeon room.
    def setEnemyNumber(self):
        self.enemyNumber = len(self.enemyList)
      
    # Summary:
    # Set whether the room has a chest or not.
    def setHasChest(self, _hasChest):
        if type(_hasChest) is bool:    
            self.hasChest = _hasChest
        else:
            raise TypeError("DungeonRoom hasChest expected a bool. Received: " + str(type(_hasChest)) + " Check the type")