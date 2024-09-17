from print_delay import PrintText
from random import randint, choice

class Item:
  def __init__(self):
    self.name = None
    self.equipSlot = None
    self.stats = {}

  def item_stats(self):
    PrintText.Print_with_delay(f"{self.name} improves:\n")
    for key, value in self.stats.items():
      PrintText.Print_with_delay(f"  {key} by {value}\n")
    print("")

class RustyHelm(Item):
  def __init__(self):
    super().__init__()
    self.name = "Rusty Helm"
    self.equipSlot = "head"
    self.stats["maxHealth"] = randint(5, 10)
    self.stats["strength"] = randint(1, 3)
    self.stats["physicalDef"] = randint(1, 3)

class ClothCap(Item):
  def __init__(self):
    super().__init__()
    self.name = "Cloth Cap"
    self.equipSlot = "head"
    self.stats["maxHealth"] = randint(3, 7)
    self.stats["maxMagic"] = randint(1, 3)
    self.stats["intellect"] = randint(1, 3)
    self.stats["magicDef"] = randint(1, 3)

class RustyMail(Item):
  def __init__(self):
    super().__init__()
    self.name = "Rusty Mail"
    self.equipSlot = "body"
    self.stats["maxHealth"] = randint(8, 15)
    self.stats["physicalDef"] = randint(2, 5)

class FrayedRobe(Item):
  def __init__(self):
    super().__init__()
    self.name = "Frayed Robe"
    self.equipSlot = "body"
    self.stats["maxHealth"] = randint(5, 10)
    self.stats["maxMagic"] = randint(3, 7)
    self.stats["intellect"] = randint(1, 3)
    self.stats["magicDef"] = randint(2, 5)

class LeatherSandals(Item):
  def __init__(self):
    super().__init__()
    self.name = "Leather Sandals"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(4, 8)
    self.stats["physicalDef"] = randint(1, 3)

class ClothSandals(Item):
  def __init__(self):
    super().__init__()
    self.name = "Cloth Sandals"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(1, 5)
    self.stats["magicDef"] = randint(1, 3)

class AdventuringPants(Item):
  def __init__(self):
    super().__init__()
    self.name = "Adventuring Pants"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(5, 10)
    self.stats["strength"] = randint(1, 3)
    self.stats["physicalDef"] = randint(2, 5)

class WanderingPants(Item):
  def __init__(self):
    super().__init__()
    self.name = "Wandering Pants"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(3, 7)
    self.stats["maxMagic"] = randint(2, 5)
    self.stats["intellect"] = randint(1, 3)
    self.stats["magicDef"] = randint(2, 5)

class ShortSword(Item):
  def __init__(self):
    super().__init__()
    self.name = "Short Sword"
    self.equipSlot = "Weapon"
    self.stats["strength"] = randint(5, 10)
    self.stats["intellect"] = randint(3, 5)

class GnarledStaff(Item):
  def __init__(self):
    super().__init__()
    self.name = "Gnarled Staff"
    self.equipSlot = "weapon"
    self.stats["maxMagic"] = randint(5, 10)
    self.stats["intellect"] = randint(8, 15)
    self.stats["strength"] = randint(3, 5)

class GreenRing(Item):
  def __init__(self):
    super().__init__()
    self.name = "Green Ring"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = randint(8, 15)
    self.stats["maxMagic"] = randint(5, 10)
    self.stats["physicalDef"] = randint(3, 7)
    self.stats["magicDef"] = randint(3, 7)

class HornedHelm(Item):
  def __init__(self):
    super().__init__()
    self.name = "Horned Helm"
    self.equipSlot = "head"
    self.stats["maxHealth"] = randint(10, 20)
    self.stats["strength"] = randint(3, 6)
    self.stats["physicalDef"] = randint(2, 4)

class HeavyHelm(Item):
  def __init__(self):
    super().__init__()
    self.name = "Heavy Helm"
    self.equipSlot = "head"
    self.stats["maxHealth"] = randint(20, 30)
    self.stats["strength"] = randint(2, 4)
    self.stats["physicalDef"] = randint(3, 6)

class WitchHat(Item):
  def __init__(self):
    super().__init__()
    self.name = "Witch Hat"
    self.equipSlot = "head"
    self.stats["maxHealth"] = randint(7, 15)
    self.stats["maxMagic"] = randint(3, 6)
    self.stats["intellect"] = randint(3, 6)
    self.stats["magicDef"] = randint(2, 4)

class MysticCap(Item):
  def __init__(self):
    super().__init__()
    self.name = "Mystic Cap"
    self.equipSlot = "head"
    self.stats["maxHealth"] = randint(14, 21)
    self.stats["maxMagic"] = randint(5, 9)
    self.stats["intellect"] = randint(2, 4)
    self.stats["magicDef"] = randint(3, 6)

class SpikedMail(Item):
  def __init__(self):
    super().__init__()
    self.name = "Spiked Mail"
    self.equipSlot = "body"
    self.stats["maxHealth"] = randint(20, 30)
    self.stats["strength"] = randint(1, 3)
    self.stats["physicalDef"] = randint(3, 6)

class SolidChestplate(Item):
  def __init__(self):
    super().__init__()
    self.name = "Solid Chestplate"
    self.equipSlot = "body"
    self.stats["maxHealth"] = randint(30, 45)
    self.stats["physicalDef"] = randint(5, 8)
    self.stats["magicDef"] = randint(5, 8)

class WitchRobe(Item):
  def __init__(self):
    super().__init__()
    self.name = "Witch Robe"
    self.equipSlot = "body"
    self.stats["maxHealth"] = randint(14, 21)
    self.stats["maxMagic"] = randint(5, 10)
    self.stats["intellect"] = randint(3, 7)
    self.stats["magicDef"] = randint(3, 6)

class MysticGarb(Item):
  def __init__(self):
    super().__init__()
    self.name = "Mystic Garb"
    self.equipSlot = "body"
    self.stats["maxHealth"] = randint(20, 30)
    self.stats["maxMagic"] = randint(10, 15)
    self.stats["intellect"] = randint(2, 5)
    self.stats["magicDef"] = randint(5, 8)
    self.stats["physicalDef"] = randint(5, 8)

class SpurredGreaves(Item):
  def __init__(self):
    super().__init__()
    self.name = "Spurred Greaves"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(8, 15)
    self.stats["strength"] = randint(1, 3)
    self.stats["physicalDef"] = randint(2, 5)

class HeavyBoots(Item):
  def __init__(self):
    super().__init__()
    self.name = "Heavy Boots"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(12, 24)
    self.stats["physicalDef"] = randint(4, 7)

class WitchSlippers(Item):
  def __init__(self):
    super().__init__()
    self.name = "Witch Slippers"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(5, 10)
    self.stats["maxMagic"] = randint(3, 7)
    self.stats["magicDef"] = randint(2, 5)

class MysticSandals(Item):
  def __init__(self):
    super().__init__()
    self.name = "Mystic Sandals"
    self.equipSlot = "feet"
    self.stats["maxHealth"] = randint(10, 15)
    self.stats["magicDef"] = randint(4, 7)

class SpurredLeggings(Item):
  def __init__(self):
    super().__init__()
    self.name = "Spurred Leggings"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(10, 20)
    self.stats["strength"] = randint(3, 6)
    self.stats["physicalDef"] = randint(3, 6)

class PlateLeggings(Item):
  def __init__(self):
    super().__init__()
    self.name = "Plate Leggings"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(20, 30)
    self.stats["strength"] = randint(2, 4)
    self.stats["physicalDef"] = randint(4, 7)

class WitchPants(Item):
  def __init__(self):
    super().__init__()
    self.name = "Witch Pants"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(10, 15)
    self.stats["maxMagic"] = randint(4, 8)
    self.stats["intellect"] = randint(4, 7)
    self.stats["magicDef"] = randint(3, 6)

class MysticSlacks(Item):
  def __init__(self):
    super().__init__()
    self.name = "Mystic Slacks"
    self.equipSlot = "legs"
    self.stats["maxHealth"] = randint(14, 21)
    self.stats["maxMagic"] = randint(5, 10)
    self.stats["intellect"] = randint(2, 5)
    self.stats["magicDef"] = randint(4, 7)

class BrutalAxe(Item):
  def __init__(self):
    super().__init__()
    self.name = "Brutal Axe"
    self.equipSlot = "Weapon"
    self.stats["strength"] = randint(20, 30)
    self.stats["intellect"] = randint(4, 8)

class Defender(Item):
  def __init__(self):
    super().__init__()
    self.name = "Defender"
    self.equipSlot = "Weapon"
    self.stats["strength"] = randint(15, 20)
    self.stats["intellect"] = randint(6, 10)
    self.stats["physicalDef"] = randint(5, 10)
    self.stats["magicDef"] = randint(3, 7)

class WitchStaff(Item):
  def __init__(self):
    super().__init__()
    self.name = "Witch Staff"
    self.equipSlot = "weapon"
    self.stats["maxMagic"] = randint(15, 20)
    self.stats["intellect"] = randint(30, 40)
    self.stats["strength"] = randint(5, 8)

class MysticRod(Item):
  def __init__(self):
    super().__init__()
    self.name = "Mystic Rod"
    self.equipSlot = "weapon"
    self.stats["maxMagic"] = randint(20, 30)
    self.stats["intellect"] = randint(20, 30)
    self.stats["strength"] = randint(8, 12)
    self.stats["physicalDef"] = randint(3, 7)
    self.stats["magicDef"] = randint(5, 10)

class BlackRing(Item):
  def __init__(self):
    super().__init__()
    self.name = "Black Ring"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = randint(30, 50)
    self.stats["strength"] = randint(5, 15)
    self.stats["intellect"] = -15
    self.stats["physicalDef"] = randint(5, 15)
    self.stats["magicDef"] = 5

class WhiteRing(Item):
  def __init__(self):
    super().__init__()
    self.name = "White Ring"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = randint(30, 50)
    self.stats["maxMagic"] = randint(15, 20)
    self.stats["intellect"] = randint(5, 15)
    self.stats["strength"] = -15
    self.stats["magicDef"] = randint(5, 15)
    self.stats["physicalDef"] = 5

class StrangeRing(Item):
  def __init__(self):
    super().__init__()
    self.name = "Strange Ring"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = randint(-25, 25)
    self.stats["maxMagic"] = randint(-5, 5)
    self.stats["strength"] = randint(-5, 5)
    self.stats["intellect"] = randint(-5, 5)

class FragmentOfShadow(Item):
  def __init__(self):
    super().__init__()
    self.name = "Fragment of Shadow"
    self.equipSlot = choice(["head", "body", "legs", "feet"])
    self.stats["maxHealth"] = randint(25, 45)
    self.stats["strength"] = randint(5, 10)
    self.stats["physicalDef"] = randint(8, 12)
    self.stats["magicDef"] = randint(4, 8)

class NullFragment(Item):
  def __init__(self):
    super().__init__()
    self.name = "Null Fragment"
    self.equipSlot = choice(["head", "body", "legs", "feet"])
    self.stats["maxHealth"] = randint(15, 30)
    self.stats["maxMagic"] = randint(5, 10)
    self.stats["intellect"] = randint(8, 12)
    self.stats["physicalDef"] = randint(4, 8)
    self.stats["magicDef"] = randint(8, 12)

class VoidFragment(Item):
  def __init__(self):
    super().__init__()
    self.name = "Void Fragment"
    self.equipSlot = choice(["head", "body", "legs", "feet"])
    self.stats["maxHealth"] = randint(20, 35)
    self.stats["maxMagic"] = randint(3, 8)
    self.stats["strength"] = randint(3, 7)
    self.stats["intellect"] = randint(4, 9)
    self.stats["physicalDef"] = randint(6, 10)
    self.stats["magicDef"] = randint(6, 10)

class ChromaticRing(Item):
  def __init__(self):
    super().__init__()
    self.name = "Chromatic Ring"
    self.equipSlot = "ring"
    self.stats["maxHealth"] = randint(50, 100)
    self.stats["maxMagic"] = randint(-25, 50)
    self.stats["strength"] = randint(-15, 25)
    self.stats["intellect"] = randint(-15, 25)
    self.stats["physicalDef"] = randint(5, 15)
    self.stats["magicDef"] = randint(5, 15)

class UnwieldlyEnd(Item):
  def __init__(self):
    super().__init__()
    self.name = "Unwieldly End"
    self.equipSlot = "weapon"
    self.stats["maxHealth"] = randint(-150, 150)
    self.stats["maxMagic"] = randint(5, 15)
    self.stats["strength"] = randint(-30, 50)
    self.stats["intellect"] = randint(-30, 50)

class FragmentOfHope(Item):
  def __init__(self):
    super().__init__()
    self.name = "Fragment of Hope"
    self.equipSlot = choice(["head", "body", "legs", "feet"])
    self.stats["maxHealth"] = randint(50, 150)
    self.stats["maxMagic"] = randint(25, 50)
    self.stats["strength"] = randint(15, 25)
    self.stats["intellect"] = randint(15, 25)
    self.stats["physicalDef"] = randint(5, 15)
    self.stats["magicDef"] = randint(5, 15)