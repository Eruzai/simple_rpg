from random import randint, choice

class NewPlayerCharacter:
  def __init__(self, name):
    self.name = name
    self.job = "Novice"
    self.level = 1
    self.experience = 0
    self.experienceNeeded = 100
    self.maxHealth = randint(15, 25)
    self.maxMagic = randint(10, 20)
    self.health = self.maxHealth
    self.magic = self.maxMagic
    self.strength = randint(5, 20)
    self.intellect = randint(5, 15)
    self.armor = 0
    self.barrier = 0
    self.head = None
    self.body = None
    self.weapon = None
    self.legs = None
    self.feet = None
    self.ring = None
  
  def damage_taken(self, damage):
    self.health -= damage
    if self.health <= 0:
      print(f"{self.name} has been defeated! Oh no!")
      # game_over()
  
  def level_up(self):
    self.level += 1
    self.experienceNeeded += 100 + self.experienceNeeded * 0.25 // 1
    if self.job == "Novice":
      self.maxHealth += randint(2, 5)
      self.maxMagic += randint(1, 3)
      self.health = self.maxHealth
      self.magic = self.maxMagic
      self.strength += randint(1, 3)
      self.intellect += randint(1, 3)
    elif self.job == "Warrior":
      self.maxHealth += randint(4, 7)
      self.maxMagic += choice([0, 0, 0, 1, 2])
      self.health = self.maxHealth
      self.magic = self.maxMagic
      self.strength += randint(3, 5)
      self.intellect += choice([0, 0, 0, 1, 2])
      self.armor += choice([0, 0, 0, 0, 1, 2, 3])
      self.barrier += choice([0, 0, 0, 1])
    elif self.job == "Wizard":
      self.maxHealth += randint(2, 5)
      self.maxMagic += randint(4, 7)
      self.health = self.maxHealth
      self.magic = self.maxMagic
      self.strength += choice([0, 0, 0, 1, 2])
      self.intellect += randint(3, 5)
      self.armor += choice([0, 0, 0, 1])
      self.barrier += choice([0, 0, 0, 0, 1, 2, 3])
    print(f"{self.name} leveled up! Hurray!")
    self.display_stats()
  
  def class_change(self):
    userSelectedClass = input("What class will you choose? Warrior or Wizard?\nType War for Warrior or Wiz for Wizard! -> ")
    if userSelectedClass == "War":
      self.job = "Warrior"
      self.maxHealth += randint(15, 25)
      self.strength += randint(5, 15)
      self.armor = randint(5, 15)
      self.barrier = randint(0, 5)
      print(f"{self.name} Has changed his job to Warrior!")
      self.display_stats()
    elif userSelectedClass == "Wiz":
      self.job = "Wizard"
      self.maxHealth += randint(5, 15)
      self.maxMagic += randint(15, 25)
      self.intellect += randint(5, 15)
      self.armor = randint(0, 5)
      self.barrier = randint(5, 15)
      print(f"{self.name} Has changed his job to Wizard!")
      self.display_stats()
    else:
      print("I don't understand... try again!")
      self.class_change()
  
  def display_stats(self):
    print(f"{self.name} the {self.job}'s stats!")
    print(f"Level: {self.level}")
    print(f"Experience to next Level up: {self.experienceNeeded - self.experience}")
    print(f"Health: {self.health}/{self.maxHealth}")
    print(f"Magic: {self.magic}/{self.maxMagic}")
    print(f"Strength: {self.strength}")
    print(f"Intellect: {self.intellect}")
    print(f"armor: {self.armor}")
    print(f"barrier: {self.barrier}")
  
  def display_equipment(self):
    print(f"{self.name} the {self.job}'s equipment!")
    print(f"Head: {self.head}")
    print(f"Body: {self.body}")
    print(f"Weapon: {self.weapon}")
    print(f"Legs: {self.legs}")
    print(f"Feet: {self.feet}")
    print(f"Ring: {self.ring}")
