

from animals import Animal
from movements.walking import Walking

class Dog(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
      super().__init__(name, species, food, chip_num)
      Walking.__init__(self)
      self.shift = shift
        
        
    
    def __str__(self):
        return f"{self.name} is a {self.species}"