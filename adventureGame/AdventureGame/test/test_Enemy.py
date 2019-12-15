"""
@author: Reece Draper
"""

import unittest.mock as mock

from obj import Enemy as EnemyClass
from obj import Weapon as WeaponClass

# Test Variables/Test setup.
testLevel = 30
testIsAlive = True

# Created mockedItem with type return ItemClass.Item.
mockedEquippedWeapon = mock.Mock(spec=WeaponClass.Weapon)

def test_Enemy_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = EnemyClass.Enemy(testLevel, testIsAlive)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    assert unitUnderTest.level == testLevel
    assert unitUnderTest.isAlive == testIsAlive
    