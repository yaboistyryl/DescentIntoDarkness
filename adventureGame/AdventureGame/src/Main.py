# -*- coding: utf-8 -*-

import time
from obj import Character as CharacterClass
from obj import Inventory as InventoryClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass
from obj import DungeonRoom as DungeonRoomClass

# Make players global
player1 = None
player2 = None

def main():
    # Show the title screen
    titleScreen()
    
    # Wait for user to input a key.
    userInput = input()
    
    # Clear the terminal screen.
    for i in range(50):
        print("\n")
    
    # If the user types "skip", it allows them to skip the introduction story.
    if userInput != "skip":
        introduction()
    else:    
        playerOneName = inputPlayerName(1)
        playerTwoName = inputPlayerName(2)
        constructPlayers(playerOneName, playerTwoName)
    
    print("\nStarting Game...")
    
    # Create random dungeonRoom.
    constructDungeonRoom()
    
        
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
    print("Sir Gregos IV: \"What is your name friend?\"")
    time.sleep(4)
    
    # Function created for validation and reusability
    playerOneName = inputPlayerName(1)
    
    print("\nSir Gregos IV: \"Ahh, " + playerOneName + " it is. how about you friend?\"\n")
    time.sleep(3)
    print("Sir Gregos nods towards the second person to walk through the door")
    time.sleep(4)
    
    playerTwoName = inputPlayerName(2)
    
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
    
def inputPlayerName(_playerNumber):
    _playerInputSuccess = False
    while _playerInputSuccess == False:
        _playerName = input("Player " + str(_playerNumber) + ": \"My name is: ")
        time.sleep(2)
        if len(_playerName) <= 20 and len(_playerName) > 0:
            return _playerName
            _playerInputSuccess = True
        elif len(_playerName) <= 0:
            print("\nSir Gregos IV: \"Speak up boy, we've no time for this\"")
        else:
            print("\nSir Gregos IV: \"Hmm, that's a long name. Do you have a nickname? Perhaps one with less than 20 letters?\"")
    
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
    
def constructDungeonRoom():
    # Create dungeonRoom with random values
    dungeonRoom1 = DungeonRoomClass.dungeonRoom()
    dungeonRoom1.printDungeonRoomInfo()

constructDungeonRoom()
    