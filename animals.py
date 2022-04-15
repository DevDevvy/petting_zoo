from attractions import SnakePit, Wetlands, PettingZoo
from slithering import Cobra, Copperhead, Cottonmouth, King, Ratsnake
from swimming import Eel, Goldfish, Guppy, Shark, Trout
from walking import Bear, Dog, Goat, Llama, Tiger
from datetime import date

varmint_village = PettingZoo("Varmint Village", "pet and feed some furry friends")
slither_inn = SnakePit("Slither Inn", "slink around with some slippery sliding friends")
fish_fortress = Wetlands("Fish Fortress", "swim in the puddle with some creepy critters")

# walkers
baloo = Bear("Baloo", "Bear", "morning", "people", 22345)
stripes = Tiger("Stripes", "Tiger", "evening", "people")
spittle = Llama("Spittle", "Llama", "evening", "greens")
billy = Goat("Billy", "Goat", "morning", "everything")
finn= Dog("Finn", "Dog", "evening", "only the best")

# swimmers
feely = Eel("Feely", "Eel thing", "small stuff")
goldeen = Goldfish("Goldeen", "Pokemon", "fish food")
flounder = Guppy("Flounder", "fish", "fish food")
toofs = Shark("Toofs", "Shark", "peoples")
trudy = Trout("Trudy", "Fish", "Fish foods")

# slitherers
cody = Cobra("Cody", "Snake", "eggs")
penny = Copperhead("Penny", "snake", "bugs")
ganj = Cottonmouth("Ganj", "Snake", "rats")
james = King("James", "Snake", "fingers")
ratty = Ratsnake("Ratty", "Snake", "Mice")



varmint_village.add_animal(baloo)
varmint_village.add_animal(stripes)
varmint_village.add_animal(spittle)
varmint_village.add_animal(billy)
varmint_village.add_animal(finn)

slither_inn.add_animal(cody)
slither_inn.add_animal(penny)
slither_inn.add_animal(ganj)
slither_inn.add_animal(james)
slither_inn.add_animal(ratty)

fish_fortress.add_animal(feely)
fish_fortress.add_animal(goldeen)
fish_fortress.add_animal(flounder)
fish_fortress.add_animal(toofs)
fish_fortress.add_animal(trudy)



# print(f'{varmint_village.attraction_name} is where you can find things like')
# for animal in varmint_village.animals:
#     print(f'    *{animal.name} the {animal.species}')
    
# print(f'{slither_inn.attraction_name} is where you can find things like')
# for animal in slither_inn.animals:
#     print(f'    *{animal.name} the {animal.species}')
    
# print(f'{fish_fortress.attraction_name} is where you can find things like')
# for animal in fish_fortress.animals:
#     print(f'    *{animal.name} the {animal.species}')
    
    
slither_inn = SnakePit("The Slither Inn", "Scary snakes")
sammy = Cobra("Sammy", "anaconda", "Ice Cube")
shalene = Ratsnake("Shalene", "rat snake", "rats...duh")

slither_inn.add_animal(sammy)
slither_inn.add_animal(shalene)

print(slither_inn.last_critter_added)
# prints Shalene the rat snake