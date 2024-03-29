"""
    Descent into Darkness Command-Line RPG Game
    
    Created by:
        Reece Draper
        Alex Downing
        Ayman Choudhery
"""

import time
import random
from obj import Character as CharacterClass
from obj import DungeonRoom as DungeonRoomClass
from obj import TerminalCommands as TerminalCommandsClass

acceptableAnswers = ["walk", "hit", "inventory", "open"]

# Summary:
#   The Main function of the program. Should be the last thing called and only once.
def main():
    playersAreAlive = True
    
    # Create random dungeonRoom.
    constructDungeonRoom()
    
    while playersAreAlive == True:
        # Player Turn
        playerTurnCommand()
        
        # enemy turn
        enemyTurn()
        
        if player1.isAlive == False and player2.isAlive == False:
            playersAreAlive = False
            time.sleep(3)
            terminalCommands.clearTerminal()
            print("Your party have succumbed to the darkness...")
            time.sleep(3)
            print("\nHint: You can type 'skip' at the beginning of game - after the title screen to skip the intro")
        
        else:
            print("\n\n=== A new turn is upon thee! ===")
            print("\nThe Heroes!")
            if (player1.isAlive == True):
                print(player1.name + " has " + str(player1.healthPoints) + " healthpoints remaining!")
            else:
                print(player1.name + " has fallen")
            
            if (player2.isAlive == True):
                print(player2.name + " has " + str(player2.healthPoints) + " healthpoints remaining!")
            else:
                print(player2.name + " has fallen")
            
            print("\nThe Enemies!")
            zeroEnemies = True
            for enemy in dungeonRoom1.enemyList:
                zeroEnemies = False
                if enemy.isAlive == True:
                    print("The " + enemy.name + " has " + str(enemy.healthPoints) + " healthpoints remaining!")
                else:
                    print(enemy.name + " lies dead and twitching on the floor")
            
            if zeroEnemies == True:
                print("The room has no enemies, prehaps your intimiadating names of " + player1.name + " and " + player2.name + " scared them away!")

            if dungeonRoom1.hasChest:
                print("\nThis room has a chest")
    
    print("Thank you for playing the Descent into Darkness!")

# Summary:
#   Function to handle the input of the player names. Adds reusability, maintenance and data validation.
def inputPlayerName(_playerNumber):
    _playerInputSuccess = False
    while _playerInputSuccess == False:
        _playerName = input("Player " + str(_playerNumber) + ", please enter your name: ")
        time.sleep(2)
        if len(_playerName) <= 20 and len(_playerName) > 0:
            return _playerName
            _playerInputSuccess = True
        elif len(_playerName) <= 0:
            print("This name is too short!")
        else:
            print("Do you have a nickname? Perhaps one with less than 20 letters?\"")
    
# Summary:
#   Constructs the dungeonRoom. This can be removed and replaced with a normal construction if we no longer print the construction info.
def constructDungeonRoom():
    # Create dungeonRoom with random values
    global dungeonRoom1
    dungeonRoom1 = DungeonRoomClass.dungeonRoom()
    
def UserInput():
    # Summary: get user input, and return all lower case
    userinput = input("Please type a command here:: ")
    return userinput.lower()

def SplitInput(funcInput):
    # Summary: split input string into seperate words, return array of words
    split = funcInput.split(" ", 1) #returns an array
    return split

def CheckAction_p1(funcInput):
    # Summary: check that the command is valid
    # This is done by splitting the command into two chunks, command word and target
    # It will check command word first, then object dependant on the command
    acc_enemy = False #@ acc_enemy -> acceptable enemy - control variable for if the enemy is acceptable
    accepted = False #@ accepted -> overall control variable for if the whole command is acceptable
    enemyID = ""     #@ enemyID -> string variable to store enemy name
    commandID = ""   #@ commandID -> string variable to store command name
    try:
        commandID = funcInput[0]
    except:
        print("You haven't typed in a command!")
    else:
        # check that the command word (word 1) is in the list of commands
        for i in range (0, len(acceptableAnswers)):
            if (funcInput[0] == acceptableAnswers[i]):
                accepted = True
        # if the command is move, check that enemies are dead and chest has been opened.
        if(commandID == "move"):
            # Check if enemies are alive.
            aliveCount = 0
            zeroEnemies = True
            for enemy in dungeonRoom1.enemyList:
                zeroEnemies = False
                if enemy.isAlive == True:
                    print("\nYou cannot move to the door because a " + enemy.name + " is in the way! You must kill it before moving on!")
                    aliveCount += 1
                    accepted = False
                    # Get out of if statement
                    
                else:
                    dungeonRoom1.regenRandomDungeonRoom()
                    accepted = True                    
        
            if zeroEnemies == True:
                dungeonRoom1.regenRandomDungeonRoom()
                accepted = True 
        
        # if the command is hit, check that the enemy exists
        elif (commandID == "hit"):
            # check that there is an enemy to hit
            try:
                enemyID = funcInput[1]
            except:
                print("You need to type the name of the enemy you are hitting!")
            else:
                for i in range (0, len(dungeonRoom1.enemyList)):
                    # word 2 is the enemy identifier
                    if acc_enemy == False:
                        if (enemyID == dungeonRoom1.enemyList[i].name.lower()):
                            player1.attack(dungeonRoom1.enemyList[i])
                            acc_enemy = True

            # if the enemy does not exist, the command is invalid
            if (acc_enemy == False):
                accepted = False
                
        elif(commandID == "open"):
            if dungeonRoom1.hasChest == True:
                aliveCount = 0
                zeroEnemies = True
                for enemy in dungeonRoom1.enemyList:
                    zeroEnemies = False
                    if enemy.isAlive == True:
                        print("\nYou cannot open the chest because the " + enemy.name + " is in the way! You must kill it before moving on!")
                        aliveCount += 1
                        accepted = False
                        # Get out of if statement
                        
                if zeroEnemies == True:
                    player1.gold += dungeonRoom1.givePlayerGold()
                    print("\n" + player1.name + " now has " + str(player1.gold) + " gold!")
                    accepted = True
                        
            else:
                print("\nThere is no chest in this room!")
            accepted == True
        elif (commandID == "inventory"):
            print("Select/ed Action: Inventory - Currently not implemented.")
            accepted == True
    return accepted

def CheckAction_p2(funcInput):
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
        print("You haven't typed in a command!")
    else:
        # check that the command word (word 1) is in the list of commands
        for i in range (0, len(acceptableAnswers)):
            if (funcInput[0] == acceptableAnswers[i]):
                accepted = True
        # if the command is move, check that enemies are dead and chest has been opened.
        if(commandID == "move"):
            # Check if enemies are alive.
            aliveCount = 0
            zeroEnemies = False
            for enemy in dungeonRoom1.enemyList:
                if enemy.isAlive == True:
                    print("\nYou cannot move to the door because a " + enemy.name + " is in the way! You must kill it before moving on!")
                    aliveCount += 1
                    accepted = False
                    break
                    # Get out of if statement                
                
                else:
                    dungeonRoom1.regenRandomDungeonRoom()
                    accepted = True    
                    
            if zeroEnemies == True:
                dungeonRoom1.regenRandomDungeonRoom()
                accepted = True
                
        # if the command is hit, check that the enemy exists
        elif (commandID == "hit"):
            # check that there is an enemy to hit
            try:
                enemyID = funcInput[1]
            except:
                print("You need to type the name of the enemy you are hitting!")
            else:
                for i in range (0, len(dungeonRoom1.enemyList)):
                    # word 2 is the enemy identifier
                    if acc_enemy == False:
                        if (enemyID == dungeonRoom1.enemyList[i].name.lower()):
                            player2.attack(dungeonRoom1.enemyList[i])
                            acc_enemy = True

            # if the enemy does not exist, the command is invalid
            if (acc_enemy == False):
                accepted = False
                
        elif(commandID == "open"):
            aliveCount = 0
            zeroEnemies = True
            for enemy in dungeonRoom1.enemyList:
                zeroEnemies = False
                if enemy.isAlive == True:
                    print("\nYou cannot open the chest because the " + enemy.name + " is in the way! You must kill it before moving on!")
                    aliveCount += 1
                    accepted = False
                    # Get out of if statement
                    
            if zeroEnemies == True:
                player2.gold += dungeonRoom1.givePlayerGold()
                print("\n" + player2.name + " now has " + str(player2.gold) + " gold!")
                accepted = True
                    
            accepted == True
        elif (commandID == "inventory"):
            print("Selected Action: Inventory - Currently not implemented.")
            accepted == True
    return accepted
    
def playerTurnCommand():
    # Summary: Get user input, evaluate, loop if the input is not an acceptable command
    # Do not allow the turn to run unless the command is correct
    actionAccepted = False  #@ actionAccepted -> loop control variable
    while (actionAccepted == False):
        if(player1.isAlive == True):
            print ("\n" + player1.name + "! It is your turn!")
            userinput = UserInput()                     #@ userinput -> initial user input as a string
            splitInput = SplitInput(userinput)          #@ splitInput -> an array of strings, each string a word
            actionAccepted = CheckAction_p1(splitInput)
            
            if (actionAccepted == False):
                print("That was an incorrect command, try again")
                playerTurnCommand()
        else:
            print(player1.name + " can't take their turn because they are dead!")
            actionAccepted = True

    actionAccepted = False #reset
    while (actionAccepted == False):
        if(player2.isAlive == True):
            print ("\n" + player2.name + "! It is your turn!")
            userinput = UserInput()                     #@ userinput -> initial user input as a string
            splitInput = SplitInput(userinput)          #@ splitInput -> an array of strings, each string a word
            actionAccepted = CheckAction_p2(splitInput)
        
            if (actionAccepted == False):
                print("That was an incorrect command, try again")
                playerTurnCommand()
        else:
            print(player2.name + " can't take their turn because they are dead!")
            actionAccepted = True

def chooseVictim():
    number = random.random()
    
    if (number < 0.5) and (player1.healthPoints > 0):
        return player1
    elif (player2.healthPoints > 0):
        return player2
    elif (player1.healthPoints > 0):
        return player1
    else:
        return "don't attack"

def enemyTurn():
    for enemy in dungeonRoom1.enemyList:
        if enemy.isAlive == True:
            victim = chooseVictim()
            if (victim == "don't attack"):
                print(enemy.name + " stares at the lifeless bodies of " + player1.name + " and " + player2.name)
            else:
                attack(enemy, victim)
        else:
            print(enemy.name + " lies dead and twitching on the floor")

def attack(enemy, target): #enemy to character
    print("\n" + enemy.name + " attacked " + target.name + " for " + str(enemy.equippedWeapon.damage) + " damage!")
    target.setHealthPoints(target.healthPoints - enemy.equippedWeapon.damage)
    if (target.isAlive == True):
        print(target.name + " has " + str(target.healthPoints) + " healthpoints remaining!")
    
# Create the terminal commands controller.
terminalCommands = TerminalCommandsClass.TerminalCommands()    

# Show the title screen.
terminalCommands.clearTerminal()
terminalCommands.titleScreen()

# Wait for user to input a key.
userInput = input()

# Clear the terminal screen.
terminalCommands.clearTerminal()

# Get the player names from user.
playerOneName = inputPlayerName(1)
playerTwoName = inputPlayerName(2)

terminalCommands.clearTerminal()

if userInput.lower() != "skip":
    terminalCommands.introduction()

# Output the tutotial text to the terminal.
terminalCommands.tutorialText()

# Construct the Character objects with the players names.
player1 = CharacterClass.Character(playerOneName)
player2 = CharacterClass.Character(playerTwoName)

terminalCommands.clearTerminal()

# Run the man game.
main()