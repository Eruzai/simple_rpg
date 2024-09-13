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
    self.stats["maxHealth"] = randint(1, 10)
    self.stats["maxMagic"] = randint(1, 10)
    self.stats["strength"] = randint(1, 10)
    self.stats["intellect"] = randint(1, 10)
    self.stats["physicalDef"] = randint(1, 10)
    self.stats["magicDef"] = randint(1, 10)

class Loop(Item):
  def __init__(self):
    super().__init__()
    self.name = "Loop of Stats"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = randint(1, 10)
    self.stats["maxMagic"] = randint(1, 10)

class Robe(Item):
  def __init__(self):
    super().__init__()
    self.name = "Robe of Stats"
    self.equipSlot = "body"
    self.stats["maxMagic"] = randint(1, 10)
    self.stats["intellect"] = randint(1, 10)
    self.stats["magicDef"] = randint(1, 10)

class Pants(Item):
  def __init__(self):
    super().__init__()
    self.name = "Pants of Stats"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(1, 10)
    self.stats["strength"] = randint(1, 10)
    self.stats["physicalDef"] = randint(1, 10)

class Shoes(Item):
  def __init__(self):
    super().__init__()
    self.name = "Shoes of Stats"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(1, 10)
    self.stats["maxMagic"] = randint(1, 10)
    self.stats["intellect"] = randint(1, 10)
    self.stats["magicDef"] = randint(1, 10)

class Hat(Item):
  def __init__(self):
    super().__init__()
    self.name = "Hat of Stats"
    self.equipSlot = "head"
    self.stats["intellect"] = randint(1, 10)
    self.stats["magicDef"] = randint(1, 10)

class Sword(Item):
  def __init__(self):
    super().__init__()
    self.name = "Sword of Stats"
    self.equipSlot = "weapon"
    self.stats["strength"] = randint(1, 10)
    self.stats["intellect"] = randint(1, 10)