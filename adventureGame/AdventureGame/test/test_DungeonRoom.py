"""
@author: Reece Draper
"""

import pytest as assertion
import unittest.mock as mock

from obj import DungeonRoom as DungeonRoomClass
from obj import Enemy as EnemyClass

testName = "TestName"
testHasEnemies = True

mockedEnemy = mock.Mock(spec=EnemyClass.Enemy)
enemyList = [mockedEnemy, mockedEnemy, mockedEnemy]

testHasChest = True

def test_DungeonRoom_Constructs_With_Valid_Data():
    
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = DungeonRoomClass.dungeonRoom(testName, testHasEnemies, enemyList, testHasChest)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert that each value was set correctly.
    assert unitUnderTest.name == testName
    assert unitUnderTest.hasEnemies == testHasEnemies
    assert unitUnderTest.enemyList == enemyList
    assert unitUnderTest.hasChest == testHasChest
    
def test_DungeonRoom_fails_to_construct_with_invalid_name_type():
    
    # 3As | Arrange
    testName = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testName)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = DungeonRoomClass.dungeonRoom(testName, testHasEnemies, enemyList, testHasChest)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "DungeonRoom name expected a string. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)

def test_DungeonRoom_fails_to_construct_with_invalid_hasEnemies_type():
    
    # 3As | Arrange
    testHasEnemies = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testHasEnemies)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = DungeonRoomClass.dungeonRoom(testName, testHasEnemies, enemyList, testHasChest)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "DungeonRoom hasEnemies expected a bool. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)
    
def test_DungeonRoom_fails_to_construct_with_invalid_hasChest_type():
    
    # 3As | Arrange
    testHasChest = 1
    
    # ExpectedOutput is only used to compare the type of the output. Expect int type out.
    expectedOutput = type(testHasChest)
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = DungeonRoomClass.dungeonRoom(testName, testHasEnemies, enemyList, testHasChest)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
        
    # Assert that the correct exception was raised
    assert exc_info.errisinstance(TypeError)
    assert "DungeonRoom hasChest expected a bool. Received: " + str(expectedOutput) + " Check the type" in str(exc_info.value)