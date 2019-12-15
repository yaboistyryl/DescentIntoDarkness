import time

class TerminalCommands:

    # Summary:
    #   Prints the initial title screen at the start of the game.   
    @staticmethod
    def titleScreen():
        print("\n|==============================|")
        print("|  Welcome to Adventure Game!  |")
        print("| Enter any value to continue! |")
        print("|==============================|")

    # Summary:
    #   Clears the terminal screen by outputting 50 new lines.
    @staticmethod
    def clearTerminal():
        # Clear the terminal screen.
        for i in range(50):
            print("\n")
    
    # Summary:
    #   Outputs the tutorial text to the terminal.
    @staticmethod
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
    #   Handles the beginning of the game. Sets the scene and gathers required user information.
    @staticmethod
    def introduction():
        print("\nSir Gregos IV: \"Quickly, in here! They're too many of them!\"\n")
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
        print("Sir Gregos IV: \"here take these, I killed these fiends earlier, you'll need them\"\n")
        time.sleep(3)
        print("Sir Gregos reaches down and grabs 2 swords from dead skeletons he slayed earlier\n")
        time.sleep(4)
        print("Sir Gregos IV: \"Now go, make your way through these dungeons and do whatever it takes to reach Lansgard and get reinforcements\"\n")
        time.sleep(3)
        print("Sir Gregos IV: \"All of the kingdom here is counting on you\"\n")
        time.sleep(3)
        print("Sir Gregos IV hurries you through the door to the next room\n")
        time.sleep(4)
        print("Sir Gregos IV: \"Good luck friends\"\n")
        time.sleep(3)
        print("The door is sealed behind you as you take your first glimpse of the room...\n")
        time.sleep(3)