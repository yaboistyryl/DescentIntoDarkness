# -*- coding: utf-8 -*-

import time
import random
import unittest.mock as mock
from obj import Character as CharacterClass
from obj import Inventory as InventoryClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass
from obj import DungeonRoom as DungeonRoomClass
from obj import Enemy as EnemyClass

# Make players global
player1 = None
player2 = None

def main():
    titleScreen()
    userInput = input()
    for i in range(50):
        print("\n")
    if userInput != "skip":
        introduction()
    else:    
        playerOneName = input("Player 1: \"My name is: ")
        playerTwoName = input("Player 2: \"My name is: ")
        constructPlayers(playerOneName, playerTwoName)
    
    print("\nStarting Game...")
    
        
def titleScreen():
    print("|==============================|")
    print("|  Welcome to Adventure Game!  |")
    print("| Enter any value to continue! |")
    print("|==============================|")
    
def introduction():
    print("Sir Gregos IV: \"Quickly, in here! They're too many of them!\"\n")
    time.sleep(3)
    print("You and your friend hurry inside the ominous room where sir Gregos IV awaits, and closes the door behind you.\n")
    time.sleep(4)
    print("Sir Gregos IV: \"That's not going to hold them long, this should help\"\n")
    time.sleep(3)
    print("Sir Gregos walks over to the door and uses his formidable shield between the anchor points where normally a large plank of wood would be.\n")
    time.sleep(4)
    print("Sir Gregos IV: \"That should hold them off long enough\"\n")
    time.sleep(3)
    print("Sir Gregos IV: \"The name\'s Sir Gregos IV, long serving commander of the king\'s forces\"\n")
    time.sleep(3)
    print("Sir Gregos nods to the first of you two to walk through the door.\n")
    time.sleep(3)
    print("Sir Gregos IV: \"What is your name friend?\"\n")
    time.sleep(4)
    
    playerOneName = input("Player 1: \"My name is: ")
    
    print("\nSir Gregos IV: \"Ahh, " + playerOneName + " it is. how about you friend?\"\n")
    time.sleep(3)
    print("Sir Gregos nods towards the second person to walk through the door")
    time.sleep(4)
    
    playerTwoName = input("Player 2: \"My name is: ")
    
    print("\nSir Gregos IV: \"Great to meet you too, " + playerTwoName + ", sorry it's under such awful circumstances...\"\n")
    time.sleep(3)
    print("Sir Gregos IV: \"I killed these fiends earlier, here take these, you'll need them\"\n")
    time.sleep(3)
    print("Sir Gregos reaches down and grabs 2 swords from dead skeletons he slayed earlier\n")
    time.sleep(4)
    print("Sir Gregos IV: \"Now go, make your way through these dungeons and do whatever it takes to reach Lansgard and get reinforcements\"\n")
    time.sleep(3)
    print("Sir Gregos IV: \"" + playerOneName + ", " + playerTwoName + ", I\'m counting on you\"\n")
    time.sleep(3)
    print("Sir Gregos IV hurries you through the door to the next room\n")
    time.sleep(4)
    print("Sir Gregos IV: \"Good luck friends\"\n")
    time.sleep(3)
    print("The door is sealed behind you as you take your first glimpse of the room...\n")
    
    constructPlayers(playerOneName, playerTwoName)
    
def constructPlayers(_playerOneName, _playerTwoName):
    
    level = 1
    healthPoints = 50
    manaPoints = 50
    experience = 1
    defence = 0
    inventory = InventoryClass.Inventory()
    armourSet = ArmourSetClass.ArmourSet("Basic Armour", 0, 10)
    equippedWeapon = WeaponClass.Weapon("Basic Sword", 0, 25, 0)
    gold = 50
    
    player1 = CharacterClass.Character(_playerOneName, level, healthPoints, manaPoints, experience, defence, inventory, equippedWeapon, armourSet, gold)
    player2 = CharacterClass.Character(_playerTwoName, level, healthPoints, manaPoints, experience, defence, inventory, equippedWeapon, armourSet, gold)

    # Generate rarity
    # Rarity List:
    #   Common - 35% chance
    #   Uncommon - 30% chance
    #   Rare - 20% chance
    #   Very Rare - 10% chance
    #   Legendary - 5% chance
def generateRandomRoomRarity():
    # Generate random number between 0 and 100 return a rarity value off of it.
    randNumb = random.randint(0, 100)
    # Uncommon
    if randNumb <= 35:
        return 0
    # Common
    elif randNumb <= 65:
        return 1
    # Rare
    elif randNumb <= 85:
        return 2
    # Ultra Rare
    elif randNumb <= 95:
        return 3
    # Legendary
    elif randNumb <= 100:
        return 4
    else:
        raise Exception("You are terrible at coding if we got here")
    
    # Generate amount of enemys
    # Enemy list:
    #   No Enemies - 10% chance
    #   1 enemy - 35% chance
    #   2 enemies - 30% chance
    #   3 enemies - 25% chance
def generateRandomEnemyCount():
    # Generate random number between 0 and 100 return a rarity value off of it.
    randNumb = random.randint(0, 100)
    # No enemies in room
    if randNumb <= 10:
        return 0
    # 1 enemy in the room
    elif randNumb <= 45:
        return 1
    # 2 enemies in the room
    elif randNumb <= 75:
        return 2
    # 3 enemies in the room
    elif randNumb <= 100:
        return 3
    else:
        raise Exception("You are terrible at coding if we got here")
        
    # Genrate random chest chance
    # Chest Chance list:
    #   Chest - 90% chance
    #   No Chest - 10% chance
def generateRandomChestChance():
    randNumb = random.randint(0, 100)
    if randNumb <= 90:
        return True
    elif randNumb <= 100:
        return False
    
def generateRandomEnemyList(enemyCount):
    _enemyList = []
    
    if enemyCount == 1:
        _enemyList = [generateRandomEnemy()]
    elif enemyCount == 2:
        _enemyList = [generateRandomEnemy(), generateRandomEnemy()]
    elif enemyCount == 3:
        _enemyList = [generateRandomEnemy(), generateRandomEnemy(), generateRandomEnemy()]
    
    return _enemyList

def generateRandomEnemy():
    
    enemy1 = EnemyClass.Enemy("Skeleton", 30, 500, True, mock.Mock(spec=WeaponClass.Weapon))
    
    return enemy1

def constructRandomDungeonRoom():
    
    enemyCount = generateRandomEnemyCount()
    enemyList = generateRandomEnemyList(enemyCount)
    
    if len(enemyList) >= 1:
        hasEnemies = True
    else:
        hasEnemies = False
        
    hasChest = False
    
    # Generate rarity of the room to set the name
    roomRarity = generateRandomRoomRarity()
    
    # List of potential room names
    dungeonNames = ["Common Loot Room", "Uncommon Loot Room", "Rare loot Room", "Ultra Rare Loot Room", "Legendary Loot Room"]
    
    # Generate chest chance
    hasChest = generateRandomChestChance()
    
    dungeonRoom1 = DungeonRoomClass.dungeonRoom(dungeonNames[roomRarity], hasEnemies, enemyList, hasChest)
    
constructRandomDungeonRoom()