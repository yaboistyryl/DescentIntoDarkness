"""
@author: Reece Draper; Alex Downing; Ayman Choudhery
"""

import time
from obj import Character as CharacterClass
from obj import Inventory as InventoryClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass
from obj import DungeonRoom as DungeonRoomClass

# Make players global
player1 = None
player2 = None
acceptableAnswers = ["walk", "hit", "inventory", "open"]    #for the time being
dungeonEnemies = ["skeleton", "goblin", "kobold", "zombie"] #for the time being

# Summary:
#   The Main function of the program. Should be the last thing called and only once.
def main():
    # Show the title screen.
    titleScreen()
    inputTutorialFlag = False
    
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
    playerTurnCommand(inputTutorialFlag)
    
# Summary:
#   Prints the initial title screen at the start of the game.     
def titleScreen():
    print("|==============================|")
    print("|  Welcome to Adventure Game!  |")
    print("| Enter any value to continue! |")
    print("|==============================|")
    
# Summary:
#   Handles the beginning of the game. Sets the scene and gathers required user information.
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
    
    # Gets the name of player 2 from player 2.
    playerOneName = inputPlayerName(1)
    
    print("\nSir Gregos IV: \"Ahh, " + playerOneName + " it is. how about you friend?\"\n")
    time.sleep(3)
    print("Sir Gregos nods towards the second person to walk through the door")
    time.sleep(4)
    
    # Gets the name of player 2 from player 2.
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
    
    # Constructs the players from the data given by the user.
    constructPlayers(playerOneName, playerTwoName)

# Summary:
#   Function to handle the input of the player names. Adds reusability, maintenance and data validation.
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
    
# Summary:
#   Function that constructs the players from the names given.
def constructPlayers(_playerOneName, _playerTwoName):
    
    level = 1
    healthPoints = 50
    manaPoints = 50
    experience = 1
    defence = 0
    inventory = InventoryClass.Inventory()
    armourSet = ArmourSetClass.ArmourSet("Basic Armour", 0, 10)
    equippedWeapon = WeaponClass.Weapon()
    equippedWeapon.generateStartingWeapon()
    gold = 50
    
    player1 = CharacterClass.Character(_playerOneName, level, healthPoints, manaPoints, experience, defence, inventory, equippedWeapon, armourSet, gold)
    player2 = CharacterClass.Character(_playerTwoName, level, healthPoints, manaPoints, experience, defence, inventory, equippedWeapon, armourSet, gold)

# Summary:
#   Constructs the dungeonRoom. This can be removed and replaced with a normal construction if we no longer print the construction info.
def constructDungeonRoom():
    # Create dungeonRoom with random values
    global dungeonRoom1
    dungeonRoom1 = DungeonRoomClass.dungeonRoom()
    dungeonRoom1.printDungeonRoomInfo()
    
def UserInput():
    # Summary: get user input, and return all lower case
    userinput = input("Please type a command here:: ")
    return userinput.lower()

def SplitInput(funcInput):
    # Summary: split input string into seperate words, return array of words
    split = funcInput.split(" ", 1) #returns an array
    print(str(split))
    return split

def CheckAction(funcInput):
    # Summary: check that the command is valid
    # This is done by splitting the command into two chunks, command word and target
    # It will check command word first, then object dependant on the command
    # ["walk", "hit", "inventory", "open"] -> command words that are accepted
    # ["skeleton", "goblin", "kobold", "zombie"] -> objects that are accepted
    acc_enemy = False #@ acc_enemy -> acceptable enemy - control variable for if the enemy is acceptable
    accepted = False #@ accepted -> overall control variable for if the whole command is acceptable
    enemyID = ""     #@ enemyID -> string variable to store enemy name
    commandID = ""   #@ commandID -> string variable to store command name
    
    try:
        commandID = funcInput[0]
    except:
        print("You havent typed in a command!")
    else:
        # check that the command word (word 1) is in the list of commands
        for i in range (0, len(acceptableAnswers)):
            if (funcInput[0] == acceptableAnswers[i]):
                accepted = True

        # if the command is hit, check that the enemy exists
        if (commandID == "hit"):
            # check that there is an enemy to hit
            try:
                enemyID = funcInput[1]
            except:
                print("You need to type the name of the enemy you are hitting!")
            else:
                for i in range (0, len(dungeonRoom1.enemyList)):
                    # word 2 is the enemy identifier
                    if acc_enemy == False:
                        if (enemyID == dungeonRoom1.enemyList[i].name):
                            acc_enemy = True
                            # Put enemy damaging mechanic here

            # if the enemy does not exist, the command is invalid
            if (acc_enemy == False):
                accepted = False

    return accepted

def tutorialText():
    print("\nIn this game, you control your player by typing in a command.")
    print("\nCommands are not case sensitive, however, any misspelling will require you to retype the command.")
    print("\nThe core commands are:")
    print("    'move' - This will move you to the next room, provided there are no enemies alive in your current room.")
    print("    'open' - This will open the chest in your current room, if there is an unopened chest.")
    print("    'inventory' - This will show you the items in your inventory (you can hold 10 items in your inventory at any time).")
    print("    'hit [enemyName]' - This will allow you to deal damage to a certain enemy.")
    print("\nGood luck traveller!")
    
def playerTurnCommand(_inputTutorialFlag):
    # Summary: Get user input, evaluate, loop if the input is not an acceptable command
    # Do not allow the turn to run unless the command is correct
    actionAccepted = False  #@ actionAccepted -> loop control variable
    while (actionAccepted == False):
        if _inputTutorialFlag == False:
            tutorialText()
            #make instructions never print again.
            _inputTutorialFlag = True
        userinput = UserInput()                     #@ userinput -> initial user input as a string
        splitInput = SplitInput(userinput)          #@ splitInput -> an array of strings, each string a word
        actionAccepted = CheckAction(splitInput)
        
        if (actionAccepted == False):
            print("That was an incorrect command, try again")
            playerTurnCommand(_inputTutorialFlag)
            
main()