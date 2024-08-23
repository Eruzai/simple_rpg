from random import choice
import enemies

class Location:
  def __init__(self):
     self.enemy = None
     self.treasure = None
  
  def findTreasure(self):
    print("you've found something shiny on the ground!")
  
  def findNothing(self):
    chance = choice(self.dialogArray)
    dialog = self.dialog[chance]
    print(f"{dialog}")

  def encounterEnemy(self):
    self.enemy = self.enemies[choice(self.encounterArray)]()
    print(f"{self.enemy.name} appears before you!")
  
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
    self.enemies = [enemies.Rat,
                    enemies.MysteriousShadow]
    self.encounterArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    self.dialog = ["You nearly miss stepping on a rat. Yikes!",
                   "You walk around and take a breather, It's hard work being an adventurer!",
                   "You hear someone talking about how the fields are full of slimes these days, and some of them are really shiny!",
                   "You feel like you're being watched, and not by rats...",
                   "You hear tales of people dissapearing in town recently, maybe it's the rats?",
                   "Something of a shadow moved in the corner of your vision. It was probably nothing..."]
    self.dialogArray = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]

class FieldsOfBeginning(Location):
  def __init__(self):
    super().__init__()
    self.name = "Fields of Beginning"
    self.exploreArray = [1, 2, 2, 2, 3, 3, 3]
    self.enemies = [enemies.SmallSlime,
                    enemies.Slime,
                    enemies.Goblin,
                    enemies.ShinySlime]
    self.encounterArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3]
    self.dialog = ["You take a deep breath. The air smells so fresh here.",
                   "It's very easy to walk here, the grass is a bit spongey under your feet.",
                   "It'd be nice if the slimes didn't blend in so well with the grass...",
                   "You sit down for a bit and rest",
                   "Goblins are strong and slimes are tough.",
                   "Don't eat the slimes!",
                   "Sometimes you see something shiny move in the distance."]
    self.dialogArray = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]

class MiddlingMarrow(Location):
  def __init__(self):
    super().__init__()
    self.name = "Middling Marrow"
    self.exploreArray = [1, 2, 2, 2, 2, 2, 3, 3, 3]

class KeepOfTheEnd(Location):
  def __init__(self):
    super().__init__()
    self.name = "Keep of the End"
    self.exploreArray = [1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]
