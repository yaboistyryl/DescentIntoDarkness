from obj import Weapon as WeaponClass

def test_Weapon_Constructs_With_Valid_Data():
    # 3As | Arrange
    # Nothing, use stock test variables/test setup.
    
    # 3As | Act
    # Attempt to construct character from constructor.
    unitUnderTest = WeaponClass.Weapon()
    
    # 3As | Assert
    # Assert that unit Under Test is not null.
    assert unitUnderTest != None
    
    assert unitUnderTest.name != None
    assert unitUnderTest.value != None
    assert unitUnderTest.damage != None
    assert unitUnderTest.defence != None