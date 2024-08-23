from random import choice
import enemies

class Location:
  def __init__(self):
     self.enemy = None
     self.treasure = None
  
  def findTreasure(self):
    print("you've found something shiny on the ground!")
  
  def findNothing(self):
    print("you walk around and find nothing interesting.")

  def encounterEnemy(self):
    self.enemy = self.enemies[choice(self.encounterArray)]()
    print(f"{self.enemy.name} appears before you!")
    self.enemy.display_stats()
  
  def explore(self):
    print(f"you explore the {self.name}")
    chance = choice(self.exploreArray)
    if chance == 1:
      self.findTreasure()
    elif chance == 2:
      self.encounterEnemy()
    elif chance == 3:
      self.findNothing()

class TownOfRespite(Location):
  def __init__(self):
    super().__init__()
    self.name = "Town of Respite"
    self.exploreArray = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    self.enemies = [enemies.Rat, enemies.MysteriousShadow]
    self.encounterArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

class FieldsOfBeginning(Location):
  def __init__(self):
    super().__init__()
    self.name = "Fields of Beginning"
    self.exploreArray = [1, 2, 2, 2, 3]
    self.enemies = [enemies.SmallSlime, enemies.Slime, enemies.Goblin, enemies.ShinySlime]
    self.encounterArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3]

class MiddlingMarrow(Location):
  def __init__(self):
    super().__init__()
    self.name = "Middling Marrow"
    self.exploreArray = [1, 2, 2, 2, 2, 2, 3, 3]

class KeepOfTheEnd(Location):
  def __init__(self):
    super().__init__()
    self.name = "Keep of the End"
    self.exploreArray = [1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]
