"""
@author: Alexander Downing
"""

import pytest as assertion
# Allows us to create obj for testing.
from src import Main as main

def walking_works():
    assert main.CheckAction([ "walk" ]) == True
    assert main.CheckAction([ "walk", "north" ]) == True
    
def opening_chests_works():
    assert main.CheckAction([ "open" ]) == True
    assert main.CheckAction([ "open", "chest" ]) == True

def inventory_works():
    assert main.CheckAction([ "inventory" ]) == True
    assert main.CheckAction([ "inventory", "mine" ]) == True

def hitting_enemies_works():
    assert main.CheckAction([ "hit", "skeleton" ]) == True
    assert main.CheckAction([ "hit", "goblin" ]) == True

def hitting_nothing_doesnt_work():
    assert main.CheckAction([ "hit" ]) == False
    assert main.CheckAction([ "hit", "nothing" ]) == False
    
def typos_doesnt_work():
    assert main.CheckAction([ "hiit" ]) == False
    assert main.CheckAction([ "inventorry" ]) == False
    assert main.CheckAction([ "opn" ]) == False
    assert main.CheckAction([ "wlak" ]) == False