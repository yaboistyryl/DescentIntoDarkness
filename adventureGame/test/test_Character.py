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
testLevel = 30
testHealthPoints = 500
testManaPoints = 1000
testExperience = 150
testDefence = 500
mockedInventory = mock.Mock(spec=InventoryClass.Inventory)
mockedEquippedWeapon = mock.Mock(spec=WeaponClass.Weapon)
mockedArmourSet = mock.Mock(spec=ArmourSetClass.ArmourSet)
testGold = 100000

def test_Character_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)

    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert that each value was set correctly.
    assert unitUnderTest.name == testName
    assert unitUnderTest.level == testLevel
    assert unitUnderTest.healthPoints == testHealthPoints
    assert unitUnderTest.manaPoints == testManaPoints
    assert unitUnderTest.experience == testExperience
    assert unitUnderTest.defence == testDefence
    assert unitUnderTest.inventory == mockedInventory
    assert unitUnderTest.equippedWeapon == mockedEquippedWeapon
    assert unitUnderTest.armourSet == mockedArmourSet
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
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Character name expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_level_type():
    # 3As | Arrange        
    # Overwrite testLevel to be invalid data.
    testLevel = "This should not be a string but hey, testing ftw"
    
    # ExpectedOutput is only used to compare the type of the output. Expect string type out.
    expectedOutput = type(testLevel)
    
    # 3As | Act
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the exception was successfully raised.
    assert exc_info.errisinstance(TypeError)
    assert "Character level expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_health_points_type():
    # 3As | Arrange   
    # Overwrite testHealthPoints to be invalid data.     
    testHealthPoints = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testHealthPoints)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the exception was successfully raised. 
    assert exc_info.errisinstance(TypeError)
    assert "Character health points expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_mana_points_type():
    # 3As | Arrange    
    # Overwrite testManaPoints to be invalid data.    
    testManaPoints = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testManaPoints)
    
    # 3As | Act
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the exception was successfully raised. 
    assert exc_info.errisinstance(TypeError)
    assert "Character mana points expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_experience_type():
    # 3As | Arrange        
    # Overwrite testExperience to be invalid data.
    testExperience = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testExperience)
    
    # 3As | Act      
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the exception was successfully raised.
    assert exc_info.errisinstance(TypeError)
    assert "Character experience expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_defence_type():
    # 3As | Arrange   
    # Overwrite testDefence to be invalid data.     
    testDefence = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testDefence)
    
    # 3As | Act
    # Attempt to construct character from constructor.        
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the exception was successfully raised.
    assert exc_info.errisinstance(TypeError)
    assert "Character defence expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_Inventory_type():
    # 3As | Arrange   
    # Overwrite testDefence to be invalid data.     
    testInventory = "This should not be a string but hey, testing ftw"
    
        # Expect string type out
    expectedOutput = type(testInventory)
    
    # 3As | Act
    # Attempt to construct character from constructor.        
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, testInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True    
    
    # Assert that the exception was successfully raised. 
    assert exc_info.errisinstance(TypeError)
    assert "Character inventory expected an obj of type Inventory. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_Weapon_type():
    # 3As | Arrange   
    # Overwrite testDefence to be invalid data.     
    testEquippedWeapon = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testEquippedWeapon)
    
    # 3As | Act
    # Attempt to construct character from constructor.        
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, testEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True    
    
    # Assert that the exception was successfully raised. 
    assert exc_info.errisinstance(TypeError)
    assert "Character equippedWeapon expected an obj of type Weapon. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_ArmourSet_type():
    # 3As | Arrange   
    # Overwrite testDefence to be invalid data.     
    testArmourSet = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testArmourSet)
    
    # 3As | Act
    # Attempt to construct character from constructor.        
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, testArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True    
    
    # Assert that the exception was successfully raised. 
    assert exc_info.errisinstance(TypeError)
    assert "Character armourSet expected an obj of type ArmourSet. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Character_fails_to_construct_with_invalid_gold_type():
    # 3As | Arrange
    # Overwrite testGold to be invalid data.
    testGold = "This should not be a string but hey, testing ftw"
    
    # Expect string type out
    expectedOutput = type(testGold)
    
    # 3As | Act
    # Attempt to construct character from constructor.        
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = CharacterClass.Character(testName, testLevel, testHealthPoints, testManaPoints, testExperience, testDefence, mockedInventory, mockedEquippedWeapon, mockedArmourSet, testGold)
        
    # 3As | Assert
    # Try assert if unitUnderTest is null. If null it will throw error. Catch error and assert true.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the exception was successfully raised. 
    assert exc_info.errisinstance(TypeError)
    assert "Character gold expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)