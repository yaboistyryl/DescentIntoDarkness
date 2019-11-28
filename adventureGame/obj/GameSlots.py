# -*- coding: utf-8 -*-
"""
@author: Reece Draper
"""

debug = False

class GameSlots:
    
    # Summary:
    # Constructor - Creates an instance of the class.
    
    # Parameters:
    # int _activeGameSlot - The gameSlot that will be loaded. Default is 1.
    # GameSlot obj _gameSlot1 - The first game slot/save.
    # GameSlot obj _gameSlot2 - The second game slot/save.
    # GameSlot obj _gameSlot3 - The third game slot/save.
    
    def __init__(self, _activeGameSlot = 1, _gameSlot1, _gameSlot2, _gameSlot3):
        self.activeGameSlot = _activeGameSlot
        self.gameSlot1 = _gameSlot1
        self.gameSlot2 = _gameSlot2
        self.gameSlot3 = _gameSlot3
        
        if debug == True:
            print("\nConstructing game slots handler...\n")
            print("Active Game Slot: " + str(_activeGameSlot.name))
            
class GameSlot:
    
    # Summary:
    # Constructor - Creates an instance of the class.
    
    # Parameters:
    # str _name - The name of the save slot.
    # str _saveFile - The save file location. 
    def __init__(self, _name, _saveFile):
        self.name = _name
        self.savefile = _saveFile
        
    if debug == True:
        print("\nConstructing a Game Slot...\n")
        print("Name: " + self.name)
        print("Save File Location: " + str(self._saveFile))