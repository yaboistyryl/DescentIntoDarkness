"""
@author: Reece Draper
"""

class ArmourSet:
    
    # Summary:
    # Constructor for Character Object.
    
    # str name - The name of the armour
    # int value - The value of the armour
    # int defence - The value of the armour
    
    def __init__(self, _name, _value, _defence):
        
        # Setup obj attributes
        self.setName(_name)
        self.setValue(_value)
        self.setDefence(_defence)
    
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("ArmourSet name expected a string. Received: " + str(type(_name)) + " Check the type")
            
    def setValue(self, _value):
        if type(_value) is int:
            self.value = _value
        else:
            raise TypeError("ArmourSet value expected an int. Received: " + str(type(_value)) + " Check the type")
            
    def setDefence(self, _defence):
        if type(_defence) is int:
            self.defence = _defence
        else:
            raise TypeError("ArmourSet defence expected an int. Received: " + str(type(_defence)) + " Check the type")