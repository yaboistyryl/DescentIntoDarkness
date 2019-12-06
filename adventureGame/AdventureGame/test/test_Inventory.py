"""
@author: Reece Draper
"""

import pytest as assertion
import unittest.mock as mock

from obj import Inventory as InventoryClass
from obj import Item as ItemClass
from obj import Weapon as WeaponClass
from obj import ArmourSet as ArmourSetClass

# Create mockedItem with type return ItemClass.Item.
mockedItem = mock.Mock(spec=ItemClass.Item)

# Create mockedWeapon with type return WeaponClass.Weapon.
mockedWeapon = mock.Mock(spec=WeaponClass.Weapon)

# Create mockedArmourSet with type return ArmourSetClass.ArmourSet
mockedArmourSet = mock.Mock(spec=ArmourSetClass.ArmourSet)

def test_Inventory_Constructs_When_No_Items_Are_Given():
    # 3As | Arrange
    testItems = []
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = InventoryClass.Inventory(testItems)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None

def test_Inventory_Constructs_When_Given_One_Item():
    # 3As | Arrange
    testItems = [mockedItem]
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = InventoryClass.Inventory(testItems)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert testItems[0] != None
    assert unitUnderTest != None
    assert unitUnderTest.items[0] != None
    assert unitUnderTest.items[0] == testItems[0]
    
def test_Inventory_Constructs_When_Given_One_Weapon():
    # 3As | Arrange
    testItems = [mockedWeapon]
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = InventoryClass.Inventory(testItems)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert testItems[0] != None
    assert unitUnderTest != None
    assert unitUnderTest.items[0] != None
    assert unitUnderTest.items[0] == testItems[0]
    
def test_Inventory_Constructs_When_Given_One_ArmourSet():
    # 3As | Arrange
    testItems = [mockedArmourSet]
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = InventoryClass.Inventory(testItems)
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert testItems[0] != None
    assert unitUnderTest != None
    assert unitUnderTest.items[0] != None
    assert unitUnderTest.items[0] == testItems[0]
    
def test_Inventory_Constructs_When_Given_Ten_Items():
    # 3As | Arrange
    testItems = [mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem]
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = InventoryClass.Inventory(testItems)
    
    # 3As | Assert
    # Assert that testItems is not null
    assert testItems[0] != None
    
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    # Assert first item is equal to first test item
    assert unitUnderTest.items[0] != None
    assert unitUnderTest.items[0] == testItems[0]
    
    # Assert last item is equal to last test item
    assert unitUnderTest.items[9] != None
    assert unitUnderTest.items[9] == testItems[9]
    
def test_Inventory_Fails_To_Construct_When_Given_More_Than_Ten_Items():
    # 3As | Arrange
    testItems = [mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem, mockedItem]
    
    # 3As | Act
    # Attempt to construct character from constructor.
    with assertion.raises(Exception) as exc_info:
        unitUnderTest = InventoryClass.Inventory(testItems)
        
    # 3As | Assert
    # Assert object was not constructed.
    try:
        assert unitUnderTest == None
    except UnboundLocalError:
        assert True
    
    assert ("ERROR: Too many items for the inventory to initialise!") in str(exc_info.value)