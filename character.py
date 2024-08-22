from random import randint

class PlayerCharacter:
  def __init__(self, name):
    self.name = name
    self.job = "Novice"
    self.maxHealth = randint(15, 25)
    self.maxMagic = randint(10, 20)
    self.health = self.maxHealth
    self.magic = self.maxMagic
    self.strength = randint(5, 20)
    self.intellect = randint(5, 15)
    self.armor = 0
    self.barrier = 0

  def class_change(self):
    userSelectedClass = input("What class will you choose? Warrior or Wizard?\nType War for Warrior or Wiz for Wizard! -> ")
    if userSelectedClass == "War":
      self.job = "Warrior"
      self.maxHealth += randint(15, 25)
      self.strength += randint(5, 15)
      self.armor = randint(5, 15)
    elif userSelectedClass == "Wiz":
      self.job = "Wizard"
      self.maxHealth += randint(5, 15)
      self.maxMagic += randint(15, 25)
      self.intellect += randint(5, 15)
      self.barrier = randint(5, 15)
    else:
      print("I don't understand... try again!")
      self.class_change()
    
  def display_stats(self):
    print(f"{self.name} the {self.job}'s stats!")
    print(f"Health: {self.health}/{self.maxHealth}")
    print(f"Magic: {self.magic}/{self.maxMagic}")
    print(f"Strength: {self.strength}")
    print(f"Intellect: {self.intellect}")
    print(f"armor: {self.armor}")
    print(f"barrier: {self.barrier}")

userInputName = input("You start playing as a Novice!\nGive your character a name -> ")

player1 = PlayerCharacter(userInputName)
player2 = PlayerCharacter(userInputName)

player1.display_stats()
player2.display_stats()

player1.class_change()
player2.class_change()

player1.display_stats()
player2.display_stats()