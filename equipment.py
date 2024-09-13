from random import randint

class Item:
  def __init__(self):
    self.name = None
    self.equipSlot = None
    self.stats = {}

  def item_stats(self):
    print(f"{self.name} improves:")
    for key, value in self.stats.items():
      print(f"  {key} by {value}")

class Ring(Item):
  def __init__(self):
    super().__init__()
    self.name = "Ring of Stats"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = 150
    self.stats["maxMagic"] = 50
    self.stats["strength"] = 50
    self.stats["intellect"] = 50
    self.stats["physicalDef"] = 15
    self.stats["magicDef"] = 15

class Loop(Item):
  def __init__(self):
    super().__init__()
    self.name = "Loop of Stats"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = 200
    self.stats["maxMagic"] = 100

class Robe(Item):
  def __init__(self):
    super().__init__()
    self.name = "Robe of Stats"
    self.equipSlot = "body"
    self.stats["maxMagic"] = 50
    self.stats["intellect"] = 50
    self.stats["magicDef"] = 15