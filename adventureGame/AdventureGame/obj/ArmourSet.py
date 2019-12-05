"""
@author: Reece Draper

TO DO:
    Make this randomly generated with rarity.
    Rarity percentages should match that of Weapon.
"""

class ArmourSet:
    
    # Summary:
    #   Constructor for Character Object.
    # @Params:
    #   str name - The name of the armour
    #   int value - The value of the armour
    #   int defence - The value of the armour
    def __init__(self, _name, _value, _defence):
        
        # Setup obj attributes
        self.setName(_name)
        self.setValue(_value)
        self.setDefence(_defence)
    
    # Summary:
    #   Sets the name of the ArmourSet.
    # @Param:
    #   string _name - The name fo the ArmourSet.
    def setName(self, _name):
        if type(_name) is str:
            self.name = _name
        else:
            raise TypeError("ArmourSet name expected a string. Received: " + str(type(_name)) + " Check the type")
      
    # Summary:
    #   Sets the value of the ArmourSet.
    # @Param:
    #   int _value - The value of the ArmourSet.
    def setValue(self, _value):
        if type(_value) is int:
            self.value = _value
        else:
            raise TypeError("ArmourSet value expected an int. Received: " + str(type(_value)) + " Check the type")
    
    # Summary:
    #   Sets the defence of the ArmourSet.
    # @Param:
    #   int _defence - The defence of the weapon.
    def setDefence(self, _defence):
        if type(_defence) is int:
            self.defence = _defence
        else:
            raise TypeError("ArmourSet defence expected an int. Received: " + str(type(_defence)) + " Check the type")