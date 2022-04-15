from attractions import SnakePit, Wetlands, PettingZoo
from animals import Cobra, Copperhead, Cottonmouth, King, Ratsnake, Eel, Goldfish, Guppy, Shark, Trout, Bear, Dog, Goat, Llama, Tiger




varmint_village = PettingZoo("Varmint Village", "pet and feed some furry friends")
slither_inn = SnakePit("Slither Inn", "slink around with some slippery sliding friends")
fish_fortress = Wetlands("Fish Fortress", "swim in the puddle with some creepy critters")

# walkers
baloo = Bear("Baloo", "Bear", "morning", "people", 22345)
stripes = Tiger("Stripes", "Tiger", "evening", "people", 34636)
spittle = Llama("Spittle", "Llama", "evening", "greens", 3567)
billy = Goat("Billy", "Goat", "morning", "everything", 98765)
finn= Dog("Finn", "Dog", "evening", "only the best", 2985)

# swimmers
feely = Eel("Feely", "Eel thing", "small stuff", 83724)
goldeen = Goldfish("Goldeen", "Pokemon", "fish food", 8362)
flounder = Guppy("Flounder", "fish", "fish food", 9575)
toofs = Shark("Toofs", "Shark", "peoples", 82463)
trudy = Trout("Trudy", "Fish", "Fish foods", 29856)

# slitherers
cody = Cobra("Cody", "Snake", "eggs", 854739)
penny = Copperhead("Penny", "snake", "bugs", 2956)
ganj = Cottonmouth("Ganj", "Snake", "rats", 294738)
james = King("James", "Snake", "fingers", 29473)
ratty = Ratsnake("Ratty", "Snake", "Mice", 56789)



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

print(spittle.feed())