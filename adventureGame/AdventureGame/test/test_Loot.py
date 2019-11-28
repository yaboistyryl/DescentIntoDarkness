"""
@author: Reece Draper
"""

import pytest as assertion
# Allows us to create obj for testing.
from obj import Item as ItemClass
# Allows us to initialise our unitUnderTest
from obj import Loot as LootClass
# Allows us to create mock obj for testing. Mock is used to create loose coupling and lose dependancy on ItemClass
import unittest.mock as mock

mockedItem = mock.Mock(spec=ItemClass.item)
testGold = 500

def test_Loot_Constructs_When_Given_Valid_Data():
    # 3As | Arrange
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = LootClass.Loot(mockedItem, testGold)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    assert unitUnderTest.item != None
    assert unitUnderTest.gold != None
    
    assert unitUnderTest.item == mockedItem
    assert unitUnderTest.gold == testGold
    
def test_Loot_Does_Not_Construct_When_Given_Invalid_Item():
    # 3As | Arrange
    testItem = "This shouldn't construct"
    
    expectedOutput = type(testItem)
    
    # 3As | Act
    # Attempt to construct Loot from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = LootClass.Loot(testItem, testGold)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    assert exc_info.errisinstance(TypeError)
    assert "Loot item expected an obj Item. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Loot_Does_Not_Construct_When_Given_Invalid_Gold():
    # 3As | Arrange
    testGold = "This shouldn't construct"
    
    expectedOutput = type(testGold)
    
    # 3As | Act
    # Attempt to construct Loot from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = LootClass.Loot(mockedItem, testGold)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    assert exc_info.errisinstance(TypeError)
    assert "Loot gold expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)