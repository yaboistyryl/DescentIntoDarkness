# -*- coding: utf-8 -*-

import time

def main():
    titleScreen()
    introduction()
        
def titleScreen():
    print("|==============================|")
    print("|  Welcome to Adventure Game!  |")
    print("| Enter any value to continue! |")
    print("|==============================|")
    input()
    for i in range(50):
        print("\n")
    
def introduction():
    print("Sir Gregos IV: \"Quickly, in here! They're too many of them!\"\n")
    time.sleep(3)
    print("You and your friend hurry inside the ominous room where sir Gregos IV awaits, closing the door behind you.\n")
    time.sleep(4)
    print("Sir Gregos IV: \"That's not going to hold them long, this should help\"\n")
    time.sleep(3)
    print("Sir Gregos walks over to the door and uses his formidable shield between the anchor points where normally a large plank of wood would be.\n")
    time.sleep(4)
    print("Sir Gregos IV: \"That should hold them off long enough\"\n")
    time.sleep(3)
    print("Sir Gregos IV: \"The names Sir Gregos IV, long serving commander of the king\'s forces\"\n")
    time.sleep(3)
    print("Sir Gregos IV: \"and your name is?\"\n")
    time.sleep(3)
    print("Sir Gregos points to the first of you two to walk through the door.")
    time.sleep(4)
    playerOneName = input("Player 1: \"my name is: ")
    print("\nSir Gregos IV: \"Ahh, " + playerOneName + " it is. how about you friend?\"\n")
    time.sleep(3)
    print("Sir Gregos points towards the second to walk through the door")
    time.sleep(4)
    playerTwoName = input("Player 2: \"My name is: ")
    print("\nSir Gregos IV: \"Great to meet you too, " + playerTwoName + ", sorry it's under such awful circumstances...\"\n")
    
    
main()