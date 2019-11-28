"""
@author: Reece Draper
"""

import pytest as assertion
from obj import ArmourSet as ArmourSetClass

testName = "TestName"
testValue = 500
testDefence = 1000

def test_ArmourSet_Constructs_With_Valid_Data():
    
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = ArmourSetClass.ArmourSet(testName, testValue, testDefence)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    assert unitUnderTest.name == testName
    assert unitUnderTest.value == testValue
    assert unitUnderTest.defence == testDefence
    
def test_ArmourSet_Does_Not_Construct_With_Invalid_Name():
    # 3As | Arrange
    testName = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testName)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ArmourSetClass.ArmourSet(testName, testValue, testDefence)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "ArmourSet name expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_ArmourSet_Does_Not_Construct_With_Invalid_Value():
    # 3As | Arrange
    testValue = "Boaty McBoatface"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testValue)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ArmourSetClass.ArmourSet(testName, testValue, testDefence)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "ArmourSet value expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_ArmourSet_Does_Not_Construct_With_Invalid_Defence():
    # 3As | Arrange
    testDefence = "Boaty McBoatface"
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testDefence)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = ArmourSetClass.ArmourSet(testName, testValue, testDefence)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "ArmourSet defence expected an int. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)