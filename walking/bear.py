from datetime import date

class Bear():
    
    def __init__(self, name, species, shift, food, chip_num):
      self.name = name
      self.species = species
      self.date_added = date.today()
      self.walking = True
      self.shift = shift
      self.food = food
      self.__chip_number = chip_num
    # setting class data type enforcer
    @property
    # getter returns privately scoped attribute
    def chip_num(self):
      return self.__chip_number
    # setter prevents user from changing chip_number value to keep permanent
    @chip_num.setter
    def chip_number(self, number):
      pass
      
    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
      
    def __str__(self):
        return f"{self.name} is a {self.species}"
      
