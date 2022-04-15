


from attractions import Attraction


class SnakePit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.animals = list()
        
    @property
    def last_critter_added(self):
        return f'{self.animals[-1]}'
        
    def add_animal(self, animal):
        self.animals.append(animal)
