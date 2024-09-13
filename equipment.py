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

class RingOfStats(Item):
  def __init__(self):
    super().__init__()
    self.name = "Ring of Stats"
    self.equipSlot = "ring"
    self.stats["health"] = 150
    self.stats["strength"] = 50
    self.stats["intellect"] = 50
    self.stats["magic"] = 50
    self.stats["physicalDef"] = 15
    self.stats["magicDef"] = 15