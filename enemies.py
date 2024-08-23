from random import randint

class Enemy:
  def __init__(self) -> None:
    pass

  def damage_taken(self, damage):
    self.health -= damage
    if self.health <= 0:
      print(f"{self.name} has been vanquished!")
      # end_encounter()
  
  def display_stats(self):
    print(f"You reveal {self.name}'s secrets!")
    print(f"Level: {self.level}")
    print(f"Health: {self.health}")
    print(f"Strength: {self.strength}")
    print(f"Intellect: {self.intellect}")
    if hasattr(self, 'armor'):
      print(f"Armor: {self.armor}")
    if hasattr(self, 'barrier'):
      print(f"Barrier: {self.barrier}")

class Rat(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rat"
    self.level = randint(1, 2)
    self.experience = 15 * (1.15 ** self.level) // 1
    self.health = randint(2, 3) * (1.25 ** self.level) // 1
    self.strength = randint(1, 2) * (1.25 ** self.level) // 1
    self.intellect = 0

class MysteriousShadow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Mysterious Shadow"
    self.level = 20
    self.experience = 100000
    self.health = 100
    self.strength = 100
    self.intellect = 100
    self.armor = 30
    self.barrier = 30

class SmallSlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Slime"
    self.level = randint(1, 3)
    self.experience = 15 * (1.5 ** self.level) // 1
    self.health = randint(2, 5) * (1.5 ** self.level) // 1
    self.strength = randint(1, 3) * (1.15 ** self.level) // 1
    self.intellect = 0
    self.armor = randint(15, 30)

class Slime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Slime"
    self.level = randint(1, 5)
    self.experience = 30 * (1.5 ** self.level) // 1
    self.health = randint(5, 10) * (1.5 ** self.level) // 1
    self.strength = randint(1, 5) * (1.15 ** self.level) // 1
    self.intellect = 0
    self.armor = randint(25, 40)

class Goblin(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Goblin"
    self.level = randint(1, 5)
    self.experience = 50 * (1.5 ** self.level) // 1
    self.health = randint(5, 10) * (1.15 ** self.level) // 1
    self.strength = randint(3, 5) * (1.35 ** self.level) // 1
    self.intellect = 0

class ShinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Shiny Slime"
    self.level = randint(5, 7)
    self.experience = 100 * (1.5 ** self.level) // 1
    self.health = randint(7, 10) * (1.5 ** self.level) // 1
    self.strength = randint(3, 5) * (1.25 ** self.level) // 1
    self.intellect = randint(3, 5) * (1.25 ** self.level) // 1
    self.armor = randint(35, 50)
    self.barrier = randint(35, 70)
