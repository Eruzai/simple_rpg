from random import choice

class Location:
  def __init__(self) -> None:
     pass
  
  def findTreasure(self):
    print("you've found something shiny on the ground!")
  
  def findNothing(self):
    print("you walk around and find nothing interesting.")

  def encounterEnemy(self):
    print("An enemy appears before you!")
  
  def explore(self):
    print(f"you explore the {self.name}")
    chance = choice(self.choiceArray)
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
    self.choiceArray = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

class FieldsOfBeginning(Location):
  def __init__(self):
    super().__init__()
    self.name = "Fields of Beginning"
    self.choiceArray = [1, 2, 2, 2, 3]

class MiddlingMarrow(Location):
  def __init__(self):
    super().__init__()
    self.name = "Middling Marrow"
    self.choiceArray = [1, 2, 2, 2, 2, 2, 3, 3]

class KeepOfTheEnd(Location):
  def __init__(self):
    super().__init__()
    self.name = "Keep of the End"
    self.choiceArray = [1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]
