import Main as mainClass

class playerTurn:
    def __init__(self):
        print("\n")
    
    def tutorialText():
        print("\nIn this game, you control your player by typing in a command.")
        print("\nCommands are not case sensitive, however, any misspelling will require you to retype the command.")
        print("\nThe core commands are:")
        print("    'move' - This will move you to the next room, provided there are no enemies alive in your current room.")
        print("    'open' - This will open the chest in your current room, if there is an unopened chest.")
        print("    'inventory' - This will show you the items in your inventory (you can hold 10 items in your inventory at any time).")
        print("    'hit [enemyName]' - This will allow you to deal damage to a certain enemy.")
        print("\nGood luck traveller!")
    
    # Summary: 
    # get user input, and return all lower case
    def UserInput():
        userinput = input("Please type a command here:: ")
        return userinput.lower()
    
    # Summary:
    # split input string into seperate words, return array of words
    def SplitInput(funcInput):
        split = funcInput.split(" ", 1) # returns an array
        print(str(split))
        return split
    
    # Summary: 
    # check that the command is valid
    def CheckAction(funcInput):
        # This is done by splitting the command into two chunks, command word and target
        # It will check command word first, then object dependant on the command
        acc_enemy = False   #@ acc_enemy -> acceptable enemy - control variable for if the enemy is acceptable
        accepted = False    #@ accepted -> overall control variable for if the whole command is acceptable
        enemyID = ""        #@ enemyID -> string variable to store enemy name
        commandID = ""      #@ commandID -> string variable to store command name
        acceptableAnswers = ["walk", "hit", "inventory", "open"]    #for the time being
        
        # WORD 1 CHECKING
        # Check that the word exists, prevents no input crashes
        try:
            commandID = funcInput[0]
        
        except:
            print("You haven't typed in a command!")
            accepted = False
        
        else:
            # check that the command word (word 1) is in the list of commands
            for i in range (0, len(acceptableAnswers)):
                if (funcInput[0] == acceptableAnswers[i]):
                    accepted = True
                    
            # if the command is move, check that enemies are dead and chest has been opened.
            if(commandID == "move"):
                
                # Check if enemies are alive.
                aliveCount = 0
                for enemy in mainClass.dungeonRoom1.enemyList:
                    if enemy.isAlive == True:
                        print("\nYou cannot move to the door because a " + enemy.name + " is in the way! You must kill it before moving on!")
                        aliveCount += 1
                        accepted = False #This line was a problem
                        break
                        # Get out of  for loop           
                    
                if aliveCount == 0:
                    # Check if chest is available to open
                    if mainClass.dungeonRoom1.hasChest == True:
                        exitCondition = False
                        leaveRoom = False
                        
                        # Get confirmation of room exit
                        while exitCondition == False:
                            userInput = input("This room has chest that you can open. Would you still like to proceed in changing rooms?\n")
                            userInput.lower()
                            
                            if userInput == "no":
                                print("\nYou turn away from the door, looking back into the room")
                                exitCondition = True
                                leaveRoom = False
                                
                            elif userInput == "yes":
                                print("\nYou open the door and enter the next room")
                                exitCondition = True
                                leaveRoom = True
                                
                            else:
                                print("You decide to ponder your decision for a little longer")
                            
                        if leaveRoom == True:
                            mainClass.dungeonRoom1.regenRandomDungeonRoom()
                            
                    accepted = True                    
            
            # WORD 2 CHECKING
            # if the command is hit, check that the enemy exists
            elif (commandID == "hit"):
                # check that there is an enemy to hit
                try:
                    enemyID = funcInput[1]
                    
                except:
                    print("You need to type the name of the enemy you are hitting!")
                    accepted = False
                    
                else:
                    for i in range (0, len(mainClass.dungeonRoom1.enemyList)):
                        # word 2 is the enemy identifier
                        if acc_enemy == False:
                            if (enemyID == mainClass.dungeonRoom1.enemyList[i].name.lower()):
                                mainClass.player1.attack(mainClass.dungeonRoom1.enemyList[i])
                                mainClass.dungeonRoom1.printEnemyListInfo()
                                acc_enemy = True
    
                # if the enemy does not exist, the command is invalid
                if (acc_enemy == False):
                    accepted = False
                    print("That enemy is not in the room!")
                    
            elif(commandID == "open"):
                print("Selected Action: Open - Currently not implemented.")
                accepted == False
                
            elif (commandID == "inventory"):
                print("Selected Action: Inventory - Currently not implemented.")
                accepted == False
                
        return accepted

    # Summary: 
    # Get user input, evaluate, loop if the input is not an acceptable command
    def playerTurnCommand(inputTutorialFlag):
        # Do not allow the turn to run unless the command is correct
        actionAccepted = False  #@ actionAccepted -> loop control variable
        while (actionAccepted == False):
            if inputTutorialFlag == False:
                playerTurn.tutorialText()
                #make instructions never print again.
                inputTutorialFlag = True
                
            userinput = playerTurn.UserInput()                     #@ userinput -> initial user input as a string
            splitInput = playerTurn.SplitInput(userinput)          #@ splitInput -> an array of strings, each string a word
            actionAccepted = playerTurn.CheckAction(splitInput)    # This will run the command if it is valid
            
            if (actionAccepted == False):
                print("That was an incorrect command, try again")
                playerTurn.playerTurnCommand(inputTutorialFlag)

playerTurn.playerTurnCommand(True)