from random import randint

class TownOfRespite:
  name = "Town of Respite"

  def findTreasure(self):
    print("you've found something shiny on the ground!")
  
  def nothingInteresting(self):
    print("you walk around and find nothing interesting.")

  def explore(self):
    chance = randint(1, 50)
    if chance == 1:
      self.findTreasure(self)
    elif chance > 1:
      self.nothingInteresting(self)

class FieldsOfBeginning:
  name = "Fields of Beginning"

  def findTreasure(self):
    print("You stumble across a treasure lying in the grass!")
    # roll chance to find out what loot is

  def encounterEnemy(self):
    print("An enemy appears before you!")
    # roll chance to find out what the enemy is

  def explore(self):
    chance = randint(1, 5)
    if chance == 1:
      self.findTreasure(self)
    elif chance > 1:
      self.encounterEnemy(self)
