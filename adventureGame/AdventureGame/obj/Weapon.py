"""
@author: Reece Draper
"""

debug = False

class Weapon:
    
    # Summary:
    # Constructor - Creates an instance of the class.  
    
    # Parameters:
    # str _name - The name of the weapon.
    # int _value - The value of the weapon.
    # int _damage - The amount of damage the weapon deals.
    # int _defence - The amount of defense the weapon provides when equipped.
    def __init__(self, _name, _value, _damage, _defence):
        
        self.setName(_name)
        self.setValue(_value)
        self.setDamage(_damage)
        self.setDefence(_defence)
        
        if debug == True:
            print("\nConstructing Weapon...\n")
            print("Name: " + self.name)
            print("Value: " + self.value)
            print("Damage: " + self.damage)
            print("Defence: " + self.defence)
    
    # Summary:
    # Set the name of the weapon.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("Weapon name expected a string. Received: " + str(type(_name)) + " Check the type")
    
    # Summary:
    # Set the value of the weapon.
    def setValue(self, _value):
        if type(_value) is int:
            self.value = _value
        else:
            raise TypeError("Weapon value expected an int. Received: " + str(type(_value)) + " Check the type")
        
    # Summary:
    # Set the damage of the weapon.
    def setDamage(self, _damage):
        if type(_damage) is int:
            self.damage = _damage
        else:
            raise TypeError("Weapon damage expected an int. Received: " + str(type(_damage)) + " Check the type")
        
    # Summary:
    # Set the defence of the weapon.
    def setDefence(self, _defence):
        if type(_defence) is int:
            self.defence = _defence
        else:
            raise TypeError("Weapon defence expected an int. Received: " + str(type(_defence)) + " Check the type")
