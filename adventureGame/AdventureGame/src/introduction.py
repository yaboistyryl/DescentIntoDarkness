# General Comments:

#   Please keep the naming of classes and class files to capital letter at start and for every new word.

#   @Staticmethod only needs to be defined when creating a function that does not use self. So I have removed self.
#   I think of self as a pointer to the instance of the class.
#   So if a car is the class and a ford mustang is an instance or a vauxhall corsa is an instance etc.

#   self is used to assign attributes. introducation is a property we want, so we assign it to self.introduction because
#   when called, it will be obj introduction.introduction and it will return "".

class Introduction:
    # Summary:
    #   Constructor
    def __init__(self):
        self.introduction = ""
    
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
    