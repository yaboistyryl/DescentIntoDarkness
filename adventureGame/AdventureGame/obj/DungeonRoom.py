# -*- coding: utf-8 -*-
"""
@author: Reece Draper
"""

from obj import Enemy as EnemyClass
import random

debug = False

class dungeonRoom:
    # Summary:
    #   Constructor - Creates an instance of the class. Generates random attributes.
    def __init__(self):
        self.enemyList = []
        self.regenRandomDungeonRoom()
            
    # Summary:
    #   Sets the name of the dungeon room.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("DungeonRoom name expected a string. Received: " + str(type(_name)) + " Check the type")
        
    # Summary:
    #   Sets whether the room has enemies or not.
    # @Param:
    #   bool _hasEnemies - Whether the dungeonRoom has enemies or not.
    def setHasEnemies(self, _hasEnemies):
        if type(_hasEnemies) is bool:
            self.hasEnemies = _hasEnemies
        else:
            raise TypeError("DungeonRoom hasEnemies expected a bool. Received: " + str(type(_hasEnemies)) + " Check the type")
    
    # Summary:
    #   Sets the enemyList of the dungeonRoom.
    # @Param:
    #   list obj Enemy _enemyList - the list of enemies that exist within the dungeonRoom. 
    def setEnemyList(self, _enemyList):
        if type(_enemyList) is list:
            if len(_enemyList) == 0:
                if debug == True:
                    print("WARNING: instance of dungeonRoom has an empty enemyList")
                self.enemyList = _enemyList
            else:
                for enemyListContent in _enemyList:
                    if isinstance(enemyListContent, EnemyClass.Enemy):
                        self.enemyList = _enemyList
                    else:
                        raise TypeError("DungeonRoom enemyList expected obj type Enemy in enemyList. Received: " + str(type(enemyListContent)) + " Check the type")
        else:
            raise TypeError("DungeonRoom enemyList expected a list. Received: " + str(type(_enemyList)) + " Check the type")
    
    # Summary:
    #   Sets the amount of enemies in the dungeon room.
    def setEnemyNumber(self):
        self.enemyNumber = len(self.enemyList)
      
    # Summary:
    # Sets whether the room has a chest or not.
    def setHasChest(self, _hasChest):
        if type(_hasChest) is bool:    
            self.hasChest = _hasChest
        else:
            raise TypeError("DungeonRoom hasChest expected a bool. Received: " + str(type(_hasChest)) + " Check the type")
    
    # Summary:        
    #   Generates a random room rarity.
    # Rarity List:
    #   Common - 35% chance
    #   Uncommon - 30% chance
    #   Rare - 20% chance
    #   Very Rare - 10% chance
    #   Legendary - 5% chance
    # return index - The random index for the dungeonNames list.
    @staticmethod
    def generateRandomRoomRarity():
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
        
    # Summary:
    #   Generates the amount of enemies.
    # Enemy list:
    #   No Enemies - 10% chance.
    #   1 enemy - 35% chance.
    #   2 enemies - 30% chance.
    #   3 enemies - 25% chance.
    # return:
    #   randomEnemyCount - the the randomly selected amount of enemies for the room.
    @staticmethod
    def generateRandomEnemyCount():
        
        randNumb = random.randint(0, 100)
        # No enemies in room
        if randNumb <= 10:
            randomEnemyCount = 0
        # 1 enemy in the room
        elif randNumb <= 45:
            randomEnemyCount = 1
        # 2 enemies in the room
        elif randNumb <= 75:
            randomEnemyCount = 2
        # 3 enemies in the room
        elif randNumb <= 100:
            randomEnemyCount = 3
        else:
            raise Exception("You are terrible at coding if we got here")
            
        return randomEnemyCount
    
    # Summary:        
    #   Generates random chest chance.
    # Chest Chance list:
    #   Chest - 90% chance.
    #   No Chest - 10% chance.
    # Return:
    #   hasChest - returns whether randomly generated room has chest.
    @staticmethod
    def generateRandomChestChance():
        
        randNumb = random.randint(0, 100)
        
        if randNumb <= 90:
            hasChest = True
        elif randNumb <= 100:
            hasChest = False
        
        return hasChest
    
    # Summary:
    #   Generates random enemy list based on the amount of enemies given.
    # @Param:
    #   enemyCount - The amount of enemies to generate in the list.
    # Return:
    #   enemyList - The list of enemies for the dungeon room.
    def generateRandomEnemyList(self, enemyCount):
        # Initialise _enemyList
        enemyList = []
        
        # Generate a random enemy equal to the amount of enemies passed in.
        #enemyList = [self.generateRandomEnemy()] * enemyCount
        
        for i in range(enemyCount):
            enemyList.append(self.generateRandomEnemy())
        
        return enemyList
    
    # Summary:
    #   Generates a random enemy for the dungeonRoom enemyList attribute.
    #   For all class methods that do not utilise 'self', it must be declared as a static method.
    @staticmethod
    def generateRandomEnemy():
        
        randEnemy = EnemyClass.Enemy(30, True)
        
        return randEnemy
    
    # Summary:
    #   Regenerates the dungeonRoom for new random values.
    def regenRandomDungeonRoom(self):
        
        # List of potential room names
        dungeonNames = ["Common Loot Room", "Uncommon Loot Room", "Rare loot Room", "Ultra Rare Loot Room", "Legendary Loot Room"]
        # Create the rarity of the room
        roomRarity = self.generateRandomRoomRarity()
        # Create final dungeonName
        dungeonName = dungeonNames[roomRarity]
        
        # Create random enemy count from 0-3
        enemyCount = self.generateRandomEnemyCount()

        # Create enemyList from amount of enemies
        enemyList = self.generateRandomEnemyList(enemyCount)
        
        # Check for duplicates in enemyList. 
        dupeCheck = self.checkDuplicateEnemies(enemyList)

        while dupeCheck == True:
            if debug == True:
                print("Duplicate Encountered! Regenerating!")
            
            # Create enemyList from amount of enemies
            enemyList = self.generateRandomEnemyList(enemyCount)
            dupeCheck = self.checkDuplicateEnemies(enemyList)
        
        # If the enemyList has one enemy or more, set boolean value hasEnemies to true.
        if len(enemyList) >= 1:
            hasEnemies = True
        else:
            hasEnemies = False
          
        # Initialise hasChest variable.
        hasChest = False
        
        # Generate chest chance.
        hasChest = self.generateRandomChestChance()
        
        # Set the new randomly generated values.
        self.setName(dungeonName)
        self.setHasEnemies(hasEnemies)
        self.setEnemyList(enemyList)
        self.setHasChest(hasChest)
    
    # Summary: 
    #   An issue was found where a player couldn't attack if there were two enemies of the same name in the dungeon room. This function will return a bool value if there is duplicate enemies in the room.
    # @Param:
    #   List obj Enemy - The enemy list you wish to check for duplicates.
    # Returns:
    #   bool duplicateCheck - Whether the list has duplicates. True for duplicates, false for no duplicates. 
    def checkDuplicateEnemies(self, _enemyList):
        
        duplicateCheck = False
        
        # Check if it's empty.
        if len(_enemyList) > 0:
            # Iterate through length of enemylist
            for i in range(len(_enemyList)):
                # Iterate through length of enemyList again to compate the two.
                for j in range(len(_enemyList)):
                    # If they're the same.
                    if _enemyList[i].name == _enemyList[j].name:
                        # Check the indexes are not the same. If they're not, then there is a duplicate.
                        if i != j:
                            duplicateCheck = True
                        
        return duplicateCheck
    
    # Summary:
    #   Prints all the information about the instance of the dungeonRoom.
    def printDungeonRoomInfo(self):
        print("\nConstructing dungeonRoom...\n")
        print("Name: " + self.name)
        print("Has Enemies: " + str(self.hasEnemies))
        print("Enemy Count: " + str(len(self.enemyList)))
        for i in range(len(self.enemyList)):
            self.enemyList[i].printEnemyInfo()
        print("\nHas Chest: " + str(self.hasChest))