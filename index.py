import datetime

class Animal:

  def __init__(self, leg_num, species, owner ="Happy Acres Farm"):
    self.owner = owner
    self.species = species
    self.leg_num = leg_num

  def set_solid_food_date(self):
    self.solid_food_date = datetime.datetime.now().strftime("%x")

  def move(self, speed):
    return f"{self.species} moves at {speed} meters per second"

class Dog(Animal):

  def __init__(self, breed):
    self.breed = breed
    super().__init__(4, "dog")

collie = Dog("collie")
print(collie)

class Horse(Animal):
  def __init__(self):
    self.races_won = []
    super().__init__(5, "horse")
  def add_won_race(self, race):
    self.races_won.append(race)

  def trot(self):
    return self.move(8)
  def gallop(self):
    return self.move(15)


buttercup = Horse()
buttercup.add_won_race("Preakness")
print(buttercup.races_won)

print(collie.leg_num)
print(buttercup.leg_num)

buttercup.set_solid_food_date()

collie.set_solid_food_date()

print(buttercup.trot())

print(buttercup.gallop())

