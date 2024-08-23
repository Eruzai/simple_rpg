from random import randint

class SmallSlime:
  def __init__(self):
    self.name = "Small Slime"
    self.level = randint(1, 3)
    self.experience = 30 * self.level // 3
    self.health = randint(2, 5) * self.level // 1.5
    self.strength = randint(1, 3)
    self.armor = randint(25, 50)

class Slime:
  def __init__(self):
    self.name = "Slime"
    self.level = randint(2, 5)
    self.experience = 30 * self.level // 5
    self.health = randint(5, 10) * self.level // 1.5
    self.strength = randint(2, 5)
    self.armor = randint(35, 50)

class Goblin:
  def __init__(self):
    self.name = "Goblin"
    self.level = randint(1, 5)
    self.experience = 50 * self.level // 5
    self.health = randint(5, 10) * self.level // 2
    self.strength = randint(1, 5) * self.level // 2

class ShinySlime:
  def __init__(self):
    self.name = "Shiny Slime"
    self.level = randint(3, 5)
    self.experience = 100 * self.level // 5
    self.health = randint(5, 10) * self.level // 2
    self.strength = randint(1, 5) * self.level // 2
    self.barrier = randint(35, 50)

class Rat:
  def __init__(self):
    self.name = "Rat"
    self.level = randint(1, 2)
    self.experience = 15 * self.level // 2
    self.health = randint(2, 3) * self.level // 2
    self.strength = randint(1, 2) * self.level // 2

class MysteriousShadow:
  def __init__(self):
    self.name = "Mysterious Shadow"
    self.level = 20
    self.experience = 100
    self.health = 100
    self.strength = 100
    self.intellect = 100
    self.armor = 30
    self.barrier = 30