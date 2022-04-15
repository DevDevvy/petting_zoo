
from attractions import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
        
    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'
    def add_animal(self, animal):
        self.animals.append(animal)

