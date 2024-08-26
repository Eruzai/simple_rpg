from random import randint

class Enemy:
  def __init__(self):
    self.name = None
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
    self.experience = 10 * (1.15 ** self.level) // 1
    self.health = randint(3, 5) * (1.25 ** self.level) // 1
    self.strength = randint(1, 2) * (1.25 ** self.level) // 1

class RabidDog(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rabid Dog"
    self.level = randint(2, 3)
    self.experience = 15 * (1.15 ** self.level) // 1
    self.health = randint(8, 12) * (1.25 ** self.level) // 1
    self.strength = randint(3, 5) * (1.5 ** self.level) // 1

class TinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Tiny Slime"
    self.level = randint(1, 3)
    self.experience = 12 * (1.15 ** self.level) // 1
    self.health = randint(8, 12) * (1.5 ** self.level) // 1
    self.strength = randint(3, 5) * (1.15 ** self.level) // 1
    self.physicalDef = randint(5, 15)

class MysteriousShadow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Mysterious Shadow"
    self.level = 20
    self.experience = 100000
    self.health = 100
    self.strength = 100
    self.intellect = 100
    self.physicalDef = 30
    self.magicDef = 30

class SmallSlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Slime"
    self.level = randint(1, 3)
    self.experience = 15 * (1.5 ** self.level) // 1
    self.health = randint(10, 15) * (1.5 ** self.level) // 1
    self.strength = randint(1, 3) * (1.15 ** self.level) // 1
    self.physicalDef = randint(15, 30)

class Slime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Slime"
    self.level = randint(2, 5)
    self.experience = 20 * (1.5 ** self.level) // 1
    self.health = randint(12, 17) * (1.5 ** self.level) // 1
    self.strength = randint(3, 5) * (1.15 ** self.level) // 1
    self.physicalDef = randint(25, 40)

class Goblin(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Goblin"
    self.level = randint(3, 5)
    self.experience = 35 * (1.5 ** self.level) // 1
    self.health = randint(7, 12) * (1.15 ** self.level) // 1
    self.strength = randint(3, 5) * (1.35 ** self.level) // 1

class SmallSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Spider"
    self.level = randint(1, 3)
    self.experience = 20 * (1.5 ** self.level) // 1
    self.health = randint(5, 12) * (1.25 ** self.level) // 1
    self.strength = randint(2, 5) * (1.25 ** self.level) // 1

class LesserWindElemental(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Lesser Wind Elemental"
    self.level = randint(3, 5)
    self.experience = 35 * (1.5 ** self.level) // 1
    self.health = randint(5, 12) * (1.35 ** self.level) // 1
    self.intellect = randint(3, 5) * (1.35 ** self.level) // 1
    self.magicDef = randint(35, 50)

class ShinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Shiny Slime"
    self.level = randint(5, 7)
    self.experience = 100 * (1.5 ** self.level) // 1
    self.health = randint(7, 10) * (1.5 ** self.level) // 1
    self.strength = randint(5, 7) * (1.25 ** self.level) // 1
    self.intellect = randint(3, 5) * (1.25 ** self.level) // 1
    self.physicalDef = randint(35, 50)
    self.magicDef = randint(35, 70)

class MarshSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Marsh Spider"
    self.level = randint(5, 8)
    self.experience = 50 * (1.5 ** self.level) // 1
    self.health = randint(8, 12) * (1.25 ** self.level) // 1
    self.strength = randint(3, 5) * (1.25 ** self.level) // 1
    self.physicalDef = randint(15, 25)

class Zombie(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Zombie"
    self.level = randint(5, 8)
    self.experience = 50 * (1.5 ** self.level) // 1
    self.health = randint(7, 12) * (1.5 ** self.level) // 1
    self.strength = randint(2, 4) * (1.15 ** self.level) // 1
    self.physicalDef = randint(15, 25)

class GiantRat(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Giant Rat"
    self.level = randint(5, 8)
    self.experience = 50 * (1.5 ** self.level) // 1
    self.health = randint(5, 8) * (1.15 ** self.level) // 1
    self.strength = randint(6, 10) * (1.25 ** self.level) // 1

class DarkSerpent(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Dark Serpent"
    self.level = randint(6, 9)
    self.experience = 65 * (1.5 ** self.level) // 1
    self.health = randint(5, 10) * (1.15 ** self.level) // 1
    self.strength = randint(3, 5) * (1.35 ** self.level) // 1

class Witch(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Witch"
    self.level = randint(7, 10)
    self.experience = 80 * (1.5 ** self.level) // 1
    self.health = randint(8, 10) * (1.25 ** self.level) // 1
    self.strength = randint(2, 5) * (1.15 ** self.level) // 1
    self.intellect = randint(7, 10) * (1.45 ** self.level) // 1
    self.magicDef = randint(40, 65)

class WretchedCrow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "WretchedCrow"
    self.level = randint(6, 8)
    self.experience = 75 * (1.5 ** self.level) // 1
    self.health = randint(5, 8) * (1.15 ** self.level) // 1
    self.strength = randint(4, 6) * (1.25 ** self.level) // 1
    self.physicalDef = randint(40, 65)

class MarshHorror(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Marsh Horror"
    self.level = randint(10, 12)
    self.experience = 150 * (1.5 ** self.level) // 1
    self.health = randint(10, 12) * (1.35 ** self.level) // 1
    self.strength = randint(2, 5) * (1.35 ** self.level) // 1
    self.intellect = randint(2, 5) * (1.35 ** self.level) // 1
    self.physicalDef = randint(30, 65)
    self.magicDef = randint(30, 65)
