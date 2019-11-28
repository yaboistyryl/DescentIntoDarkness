"""
@author: Reece Draper
"""

import pytest as assertion
import unittest.mock as mock

from obj import Enemy as EnemyClass
from obj import Weapon as WeaponClass

# Test Variables/Test setup.
testName = "TestName"
testLevel = 30
testHealthPoints = 500
testIsAlive = True

# Created mockedItem with type return ItemClass.Item.
mockedEquippedWeapon = mock.Mock(spec=WeaponClass.Weapon)

def test_Enemy_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = EnemyClass.Enemy(testName, testLevel, testHealthPoints, testIsAlive, mockedEquippedWeapon)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert that each value was set correctly.
    assert unitUnderTest.name == testName
    assert unitUnderTest.level == testLevel
    assert unitUnderTest.healthPoints == testHealthPoints
    assert unitUnderTest.isAlive == testIsAlive
    assert unitUnderTest.equippedWeapon == mockedEquippedWeapon
    
def test_Enemy_fails_to_construct_with_invalid_name_type():
    # 3As | Arrange     
    # Overwrite testName to be invalid data.
    testName = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testName)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = EnemyClass.Enemy(testName, testLevel, testHealthPoints, testIsAlive, mockedEquippedWeapon)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Enemy name expected a string. Received: " + str(expectedOutput) + " Check the type." in str(exc_info.value)
    
def test_Enemy_fails_to_construct_with_invalid_level_type():
    # 3As | Arrange     
    # Overwrite testName to be invalid data.
    testLevel = "I wonder if Ayman or Alex will ever read this. Probably not, hi Manish :)"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testLevel)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = EnemyClass.Enemy(testName, testLevel, testHealthPoints, testIsAlive, mockedEquippedWeapon)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Enemy level expected a int. Received: " + str(expectedOutput) + " Check the type." in str(exc_info.value)
    
def test_Enemy_fails_to_construct_with_invalid_healthPoints_type():
    # 3As | Arrange     
    # Overwrite testName to be invalid data.
    testHealthPoints = "I wonder if Ayman or Alex will ever read this. Probably not, hi Manish :)"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testHealthPoints)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = EnemyClass.Enemy(testName, testLevel, testHealthPoints, testIsAlive, mockedEquippedWeapon)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Enemy healthPoints expected a int. Received: " + str(expectedOutput) + " Check the type." in str(exc_info.value)
    
def test_Enemy_fails_to_construct_with_invalid_isAlive_type():
    # 3As | Arrange     
    # Overwrite testName to be invalid data.
    testIsAlive = "I wonder if Ayman or Alex will ever read this. Probably not, hi Manish :)"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testIsAlive)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = EnemyClass.Enemy(testName, testLevel, testHealthPoints, testIsAlive, mockedEquippedWeapon)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Enemy isAlive expected a bool. Received: " + str(expectedOutput) + " Check the type." in str(exc_info.value)
