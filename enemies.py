from random import randint

class Enemy:
  def __init__(self):
    self.name = None
    self.level = 0
    self.experience = 0
    self.health = 0
    self.strength = 0
    self.intellect = 0
    self.physicalDef = 0
    self.magicDef = 0

  def damage_taken(self, basedamage, attackType):
    damage = basedamage
    multiplier = 0
    if attackType == "physical":
      multiplier = self.physicalDef / 100
    elif attackType == "magical":
      multiplier = self.magicDef / 100
    damage -= basedamage * multiplier // 1
    self.health -= damage
    print(f"{self.name} takes {damage} points of {attackType} damage!")
  
  def display_stats(self):
    print(f"You reveal {self.name}'s secrets!")
    print(f"Level: {self.level}")
    print(f"Health: {self.health}")
    print(f"Strength: {self.strength}")
    print(f"Intellect: {self.intellect}")
    if hasattr(self, 'physicalDef'):
      print(f"Physical Defense: {self.physicalDef}")
    if hasattr(self, 'magicDef'):
      print(f"Magic Defense: {self.magicDef}")

class Rat(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rat"
    self.level = randint(1, 2)
    self.health = 2
    self.strength = 1
    for _ in range(self.level):
      self.experience += 2
      self.health += randint(1, 2)
      self.strength += randint(1, 2)

class RabidDog(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rabid Dog"
    self.level = randint(1, 3)
    self.experience = 8
    self.health = 4
    self.strength = 3
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(2, 4)
      self.strength += randint(1, 2)

class TinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Tiny Slime"
    self.level = randint(1, 3)
    self.experience = 5
    self.health = 8
    self.strength = 2
    self.physicalDef = 10
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(3, 5)
      self.strength += randint(1, 2)
      self.physicalDef += randint(1, 3)

class MysteriousShadow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Mysterious Shadow"
    self.level = 20
    self.experience = 100000
    self.health = 500
    self.strength = 100
    self.intellect = 100
    self.physicalDef = 50
    self.magicDef = 50

class SmallSlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Slime"
    self.level = randint(1, 3)
    self.experience = 10
    self.health = 10
    self.strength = 3
    self.physicalDef = 15
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(3, 5)
      self.strength += randint(1, 2)
      self.physicalDef += randint(3, 5)

class Slime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Slime"
    self.level = randint(1, 5)
    self.experience = 15
    self.health = 12
    self.strength = 4
    self.physicalDef = 20
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(4, 6)
      self.strength += randint(1, 3)
      self.physicalDef += randint(4, 6)

class Goblin(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Goblin"
    self.level = randint(3, 5)
    self.experience = 15
    self.health = 8
    self.strength = 4
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(2, 4)
      self.strength += randint(2, 4)

class SmallSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Spider"
    self.level = randint(1, 3)
    self.experience = 12
    self.health = 12
    self.strength = 5
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(2, 4)
      self.strength += randint(1, 3)

class LesserWindElemental(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Lesser Wind Elemental"
    self.level = randint(3, 5)
    self.experience = 20
    self.health = 15
    self.intellect = 5
    self.magicDef = 35
    for _ in range(self.level):
      self.experience += 4
      self.health += randint(3, 5)
      self.intellect += randint(2, 4)
      self.magicDef += randint(3, 7)

class ShinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Shiny Slime"
    self.level = randint(5, 7)
    self.experience = 50
    self.health = 20
    self.strength = 5
    self.intellect = 5
    self.physicalDef = 35
    self.magicDef = 35
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(4, 7)
      self.strength += randint(4, 7)
      self.intellect += randint(4, 7)
      self.physicalDef += randint(3, 7)
      self.magicDef += randint(3, 7)

class MarshSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Marsh Spider"
    self.level = randint(5, 8)
    self.experience = 25
    self.health = 12
    self.strength = 5
    self.physicalDef = 15
    for _ in range(self.level):
      self.experience += 6
      self.health += randint(2, 4)
      self.strength += randint(1, 3)
      self.physicalDef += randint(1, 3)

class Zombie(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Zombie"
    self.level = randint(5, 8)
    self.experience = 30
    self.health = 15
    self.strength = 3
    self.physicalDef = 15
    for _ in range(self.level):
      self.experience += 6
      self.health += randint(3, 5)
      self.strength += randint(1, 2)
      self.physicalDef += randint(1, 3)

class GiantRat(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Giant Rat"
    self.level = randint(5, 8)
    self.experience = 25
    self.health = 8
    self.strength = 6
    for _ in range(self.level):
      self.experience += 6
      self.health += randint(1, 3)
      self.strength += randint(2, 3)

class DarkSerpent(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Dark Serpent"
    self.level = randint(6, 9)
    self.experience = 40
    self.health = 10
    self.strength = 5
    for _ in range(self.level):
      self.experience += 8
      self.health += randint(1, 3)
      self.strength += randint(2, 4)

class Witch(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Witch"
    self.level = randint(7, 10)
    self.experience = 75
    self.health = 15
    self.strength = 5
    self.intellect = 10
    self.magicDef = 30
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(3, 5)
      self.strength += randint(1, 3)
      self.intellect += randint(3, 6)
      self.magicDef += randint(3, 5)

class WretchedCrow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "WretchedCrow"
    self.level = randint(6, 8)
    self.experience = 75
    self.health = 10
    self.strength = 4
    self.physicalDef = 40
    for _ in range(self.level):
      self.experience += 5
      self.health += randint(2, 4)
      self.strength += randint(2, 3)
      self.physicalDef += randint(3, 5)

class MarshHorror(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Marsh Horror"
    self.level = randint(10, 12)
    self.experience = 400
    self.health = 50
    self.strength = 5
    self.intellect = 2
    self.physicalDef = 40
    self.magicDef = 25
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(5, 8)
      self.strength += randint(2, 4)
      self.intellect += randint(1, 3)
      self.physicalDef += randint(2, 4)
      self.magicDef += randint(2, 4)

class WalkingArmor(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Walking Armor"
    self.level = randint(11, 15)
    self.experience = 100
    self.health = 25
    self.strength = 8
    self.physicalDef = 30
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(3, 6)
      self.strength += randint(2, 4)
      self.physicalDef += randint(1, 3)

class StoneSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Stone Spider"
    self.level = randint(11, 15)
    self.experience = 100
    self.health = 15
    self.physicalDef = 20
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(3, 5)
      self.strength += randint(1, 3)
      self.physicalDef += (1, 3)

class AncientSpectre(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Ancient Spectre"
    self.level = randint(11, 15)
    self.experience = 115
    self.health = 10
    self.strength = 3
    self.intellect = 5
    self.physicalDef = 15
    self.magicDef = 15
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(1, 5)
      self.strength += randint(1, 3)
      self.intellect += randint(2, 4)
      self.physicalDef += randint(1, 3)
      self.magicDef += randint(2, 4)

class ColumnWyrm(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Column Wyrm"
    self.level = randint(11, 15)
    self.experience = 130
    self.health = 20
    self.strength = 6
    self.intellect = 2
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(3, 5)
      self.strength += randint(2, 4)
      self.intellect += randint(1, 2)

class ShadowyCaster(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Shadowy Caster"
    self.level = randint(11, 15)
    self.experience = 130
    self.health = 10
    self.strength = 2
    self.intellect = 6
    self.physicalDef = 10
    self.magicDef = 25
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(1, 2)
      self.strength += randint(1, 2)
      self.intellect += randint(2, 4)
      self.physicalDef += randint(1, 2)
      self.magicDef += randint(2, 4)

class DancingBlades(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Dancing Blades"
    self.level = randint(11, 15)
    self.experience = 150
    self.health = 5
    self.strength = 10
    self.physicalDef = 25
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(1, 2)
      self.strength += randint(3, 6)
      self.physicalDef += randint(2, 4)

class VoidBeast(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Void Beast"
    self.level = randint(11, 15)
    self.experience = 175
    self.health = 25
    self.strength = 6
    self.intellect = 10
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(3, 6)
      self.strength += randint(1, 4)
      self.intellect += randint(1, 7)

class TheEnd(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "The End"
    self.level = 17
    self.experience = 2000
    self.health = 500
    self.strength = 25
    self.intellect = 25
    self.physicalDef = 30
    self.magicDef = 30
