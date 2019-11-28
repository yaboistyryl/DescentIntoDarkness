"""
@author: Reece Draper
"""

import pytest as assertion
from obj import Weapon as WeaponClass

# Test Variables/Test setup.
testName = "TestName"
testValue = 5000
testDamage = 100
testDefence = 50

def test_Weapon_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = WeaponClass.Weapon(testName, testValue, testDamage, testDefence)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert that each value was set correctly.
    assert unitUnderTest.name == testName
    assert unitUnderTest.value == testValue
    assert unitUnderTest.damage == testDamage
    assert unitUnderTest.defence == testDefence
    
def test_Weapon_Does_Not_Construct_With_Invalid_Name():
    # 3As | Arrange
    testName = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testName)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = WeaponClass.Weapon(testName, testValue, testDamage, testDefence)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "Weapon name expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Weapon_Does_Not_Construct_With_Invalid_Value():
    # 3As | Arrange
    testValue = "scooby dooby doo"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testValue)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = WeaponClass.Weapon(testName, testValue, testDamage, testDefence)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "Weapon value expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Weapon_Does_Not_Construct_With_Invalid_Damage():
    # 3As | Arrange
    testDamage = "Don't judge me, let me have fun with my unit tests"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testDamage)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = WeaponClass.Weapon(testName, testValue, testDamage, testDefence)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "Weapon damage expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Weapon_Does_Not_Construct_With_Invalid_Defence():
    # 3As | Arrange
    testDefence = "It's not a man purse. It's called a satchel. Indiana Jones wears one."
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testDefence)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = WeaponClass.Weapon(testName, testValue, testDamage, testDefence)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "Weapon defence expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)