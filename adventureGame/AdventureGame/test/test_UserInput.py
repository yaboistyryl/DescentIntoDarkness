"""
@author: Alexander Downing
"""

# Allows us to create obj for testing.
from src import Main as main

def test_walking_works():
    assert main.CheckAction([ "walk" ]) == True
    assert main.CheckAction([ "walk", "north" ]) == True

def test_opening_chests_works():
    assert main.CheckAction([ "open" ]) == True
    assert main.CheckAction([ "open", "chest" ]) == True

def test_inventory_works():
    assert main.CheckAction([ "inventory" ]) == True
    assert main.CheckAction([ "inventory", "mine" ]) == True

def test_hitting_enemies_works():
    assert main.CheckAction([ "hit", "skeleton" ]) == True
    assert main.CheckAction([ "hit", "goblin" ]) == True

def test_hitting_nothing_doesnt_work():
    assert main.CheckAction([ "hit" ]) == False
    assert main.CheckAction([ "hit", "nothing" ]) == False

def test_typos_doesnt_work():
    assert main.CheckAction([ "hiit" ]) == False
    assert main.CheckAction([ "inventorry" ]) == False
    assert main.CheckAction([ "opn" ]) == False
    assert main.CheckAction([ "wlak" ]) == False 