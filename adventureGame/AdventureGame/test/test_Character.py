"""
@author: Reece Draper
"""

import pytest as assertion
import unittest.mock as mock

from obj import Character as CharacterClass
from obj import Inventory as InventoryClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass


# Test Variables/Test setup.
testName = "TestName"
testLevel = 1
testHealthPoints = 50
testExperience = 0
testDefence = 0
testGold = 50

def test_Character_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = CharacterClass.Character(testName)

    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert that each value was set correctly.
    assert unitUnderTest.name == testName
    assert unitUnderTest.level == testLevel
    assert unitUnderTest.healthPoints == testHealthPoints
    assert unitUnderTest.experience == testExperience
    assert unitUnderTest.defence == testDefence
    assert isinstance(unitUnderTest.inventory, InventoryClass.Inventory)
    assert isinstance(unitUnderTest.equippedWeapon, WeaponClass.Weapon)
    assert isinstance(unitUnderTest.armourSet, ArmourSetClass.ArmourSet)
    assert unitUnderTest.gold == testGold
    
def test_Character_fails_to_construct_with_invalid_name_type():
    # 3As | Arrange     
    # Overwrite testName to be invalid data.
    testName = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testName)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Character name expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
 