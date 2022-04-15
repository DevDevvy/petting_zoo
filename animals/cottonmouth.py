
from animals import Animal
from movements.slithering import Slithering
from movements.swimming import Swimming

class Cottonmouth(Animal, Slithering, Swimming):
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      Slithering.__init__(self)
      Swimming.__init__(self)
        
        
    
    def __str__(self):
        return f"{self.name} is a {self.species}"