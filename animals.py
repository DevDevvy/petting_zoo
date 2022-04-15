from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, num):
        pass



# print(f'{varmint_village.attraction_name} is where you can find things like')
# for animal in varmint_village.animals:
#     print(f'    *{animal.name} the {animal.species}')
    
# print(f'{slither_inn.attraction_name} is where you can find things like')
# for animal in slither_inn.animals:
#     print(f'    *{animal.name} the {animal.species}')
    
# print(f'{fish_fortress.attraction_name} is where you can find things like')
# for animal in fish_fortress.animals:
#     print(f'    *{animal.name} the {animal.species}')
    
    
# slither_inn = SnakePit("The Slither Inn", "Scary snakes")
# sammy = Cobra("Sammy", "anaconda", "Ice Cube")
# shalene = Ratsnake("Shalene", "rat snake", "rats...duh")

# slither_inn.add_animal(sammy)
# slither_inn.add_animal(shalene)

# print(slither_inn.last_critter_added)
# # prints Shalene the rat snake

