

from animals import Animal

class Bear(Animal):
    
    def __init__(self, name, species, shift, food, chip_num):
      super().__init__(name, species, food, chip_num)
      self.walking = True
      self.shift = shift
    # setting class data type enforcer
    # @property
    # # getter returns privately scoped attribute
    # def chip_num(self):
    #   return self.__chip_number
    # # setter prevents user from changing chip_number value to keep permanent
    # @chip_num.setter
    # def chip_number(self, number):
    #   pass
      
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
      
