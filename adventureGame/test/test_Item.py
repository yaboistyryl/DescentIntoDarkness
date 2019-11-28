"""
@author: Reece Draper
"""

import pytest as assertion
from obj import Item as ItemClass

# Test Variables/Test setup.
testName = "TestName"
testType = "TestType"
testUsesLeft = 500
testValue = 10000

def test_Item_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = ItemClass.item(testName, testType, testUsesLeft, testValue)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert that each value was set correctly.
    assert unitUnderTest.name == testName
    assert unitUnderTest.type == testType
    assert unitUnderTest.usesLeft == testUsesLeft
    assert unitUnderTest.value == testValue
    
def test_Item_Does_Not_Construct_With_Invalid_Name():
    # 3As | Arrange
    testName = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testName)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ItemClass.item(testName, testType, testUsesLeft, testValue)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
        assert exc_info.errisinstance(TypeError)
    assert "Item name expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Item_Does_Not_Construct_With_Invalid_Type():
    # 3As | Arrange
    testType = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testType)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ItemClass.item(testName, testType, testUsesLeft, testValue)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Item type expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Item_Does_Not_Construct_With_Invalid_Uses_Left():
    # 3As | Arrange
    testUsesLeft = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz..................."
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testUsesLeft)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ItemClass.item(testName, testType, testUsesLeft, testValue)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Item usesLeft expected a int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_Item_Does_Not_Construct_With_Invalid_Value():
    # 3As | Arrange
    testValue = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz..................."
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testValue)
    
    # 3As | Act    
    # Attempt to construct character from constructor.    
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ItemClass.item(testName, testType, testUsesLeft, testValue)
    
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    # Assert that the correct exception was raised.
    assert exc_info.errisinstance(TypeError)
    assert "Item value expected a int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)