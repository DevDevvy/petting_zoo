

from animals import Animal
from movements.swimming import Swimming

class Eel(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
      super().__init__(name, species, food, chip_num)
      Swimming.__init__(self)

    
    
    def __str__(self):
        return f"{self.name} is a {self.species}"