
from animals import Animal
from movements.slithering import Slithering

class Copperhead(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      Slithering.__init__(self)
        
    
    def __str__(self):
        return f"{self.name} is a {self.species}"