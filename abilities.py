from print_delay import PrintText
from console import ConsoleCommands
from ascii_art import Draw
from random import randint, choice

class AttackMethods:
  def choose_target(self, encounter):
    if len(encounter) > 1:
      PrintText.Print_with_delay("Choose target:\n")
      for index, enemy in enumerate(encounter):
        print(f"  {index + 1} - {enemy.name}")
      self.targetIndex = int(input("enter number for target -> ")) - 1
      ConsoleCommands.clear_console()
      self.target = encounter[self.targetIndex]
    else:
      self.targetIndex = 0
      self.target = encounter[self.targetIndex]

  def random_target(self, encounter):
    self.targetIndex = randint(0, len(encounter) - 1)
    self.target = encounter[self.targetIndex]

  def random_secondary_target(self, encounter):
    targets = [x for x in encounter if x != self.target]
    self.secondaryTarget = choice(targets)


  def single_target_attack(self, encounter, name, attackType, attackDamage, numberOfAttacks, multiplier):
    AttackMethods.choose_target(self, encounter)
    Draw.attack()
    damage = attackDamage * multiplier // 1
    PrintText.Print_with_delay(f"You attack {self.target.name} with {name}!\n")
    for n in range(numberOfAttacks):
      self.target.damage_taken(damage, attackType)
  
  def random_targets_attack(self, encounter, name, attackType, attackDamage, numberOfAttacks, multiplier):
    Draw.attack()
    damage = attackDamage * multiplier // 1
    for n in range(numberOfAttacks):
      AttackMethods.random_target(self, encounter)
      PrintText.Print_with_delay(f"Your {name} hits {self.target.name}!\n")
      self.target.damage_taken(damage, attackType)

  def random_secondary_target_attack(self, encounter, name, attackType, attackDamage, numberOfAttacks, primaryMultiplier, secondaryMultiplier):
    AttackMethods.choose_target(self, encounter)
    Draw.attack()
    damage = attackDamage * primaryMultiplier // 1
    splashDamage = attackDamage * secondaryMultiplier // 1
    for n in range(numberOfAttacks):
      PrintText.Print_with_delay(f"You attack {self.target.name} with {name}!\n")
      self.target.damage_taken(damage, attackType)
      if len(encounter) > 1:
        AttackMethods.random_secondary_target(self, encounter)
        PrintText.Print_with_delay(f"Your {name} also hits {self.secondaryTarget.name}!\n")
        self.secondaryTarget.damage_taken(splashDamage, attackType)

  def all_target_attack(self, encounter, name, attackType, attackDamage, numberOfAttacks, primaryMultiplier, secondaryMultiplier):
    AttackMethods.choose_target(self, encounter)
    Draw.attack()
    damage = attackDamage * primaryMultiplier // 1
    splashDamage = attackDamage * secondaryMultiplier // 1
    for n in range(numberOfAttacks):
      PrintText.Print_with_delay(f"You target {self.target.name} with {name}!\n")
      self.target.damage_taken(damage, attackType)
      if len(encounter) > 1:
        PrintText.Print_with_delay(f"All enemies are caught in the attack!\n")
        for enemy in encounter:
          if enemy is not self.target:
            enemy.damage_taken(splashDamage, attackType)

class Attack:
  def __init__(self):
    self.name = "Attack"
    self.numberOfAttacks = 1
    self.multiplier = 1
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier)

class MagicBolt:
  def __init__(self):
    self.name = "Magic Bolt"
    self.numberOfAttacks = 1
    self.multiplier = 1
    self.abilityCost = 1
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.single_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier)
    player.magic -= self.abilityCost

class LuckyStrike:
  def __init__(self):
    self.name = "Lucky Strike"
    self.numberOfAttacks = 1
    self.multiplier = 1.25
    self.abilityCost = 3
  
  def execute(self, encounter, player):
    attackPower = choice([player.strength, player.intellect])
    attackType = choice(["physical", "magical"])
    AttackMethods.single_target_attack(self, encounter, self.name, attackType, attackPower, self.numberOfAttacks, self.multiplier)
    player.magic -= self.abilityCost

class DoubleStrike:
  def __init__(self):
    self.name = "Double Strike"
    self.numberOfAttacks = 2
    self.multiplier = 0.8
    self.abilityCost = 3
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier)
    player.magic -= self.abilityCost

class QuickCast:
  def __init__(self):
    self.name = "Quick Cast"
    self.multiplier = 0.4
    self.abilityCost = 5

  def execute(self, encounter, player):
    attackPower = player.intellect
    numberOfAttacks = randint(2, 5)
    AttackMethods.random_targets_attack(self, encounter, self.name, "magical", attackPower, numberOfAttacks, self.multiplier)
    player.magic -= self.abilityCost

class MagicBlast:
  def __init__(self):
    self.name = "Magic Blast"
    self.numberOfAttacks = 1
    self.multiplier = 1.2
    self.splashMultiplier = 0.5
    self.abilityCost = 5

  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)

class FocusMagic:
  def __init__(self):
    self.name = "Focus Magic"
    self.multiplier = 0.8
    self.abilityCost = 7

  def execute(self, encounter, player):
    attackPower = player.intellect
    numberOfAttacks = randint(1, 3)
    AttackMethods.single_target_attack(self, encounter, self.name, "magical", attackPower, numberOfAttacks, self.multiplier)
    player.magic -= self.abilityCost

class RapidStrikes:
  def __init__(self):
    self.name = "Rapid Strikes"
    self.multiplier = 0.4
  
  def execute(self, encounter, player):
    attackPower = player.strength
    numberOfAttacks = randint(2, 5)
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, numberOfAttacks, self.multiplier)

class WildStrikes:
  def __init__(self):
    self.name = "Wild Strikes"
    self.multiplier = 0.3
    self.splashMultiplier = 0.15
  
  def execute(self, encounter, player):
    attackPower = player.strength
    numberOfAttacks = randint(2, 5)
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "physical", attackPower, numberOfAttacks, self.multiplier, self.splashMultiplier)

class FocusStrike:
  def __init__(self):
    self.name = "Focus Strike"
    self.multiplier = 1.5
    self.numberOfAttacks = 1
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier)

class Cleave:
  def __init__(self):
    self.name = "Cleave"
    self.attackType = "physical"

  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "physical", attackPower, 1, 0.8, 0.5)

class ChaoticMagic:
  def __init__(self):
    self.name = "Chaotic Magic"
    self.attackType = "magical"
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.random_targets_attack(self, encounter, self.name, self.attackType, attackPower, 5, 0.6)

class Explosion:
  def __init__(self):
    self.name = "Explosion"
    self.attackType = "magical"
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.name, self.attackType, attackPower, 1, 1.5, 0.75)