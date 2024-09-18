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


  def single_target_attack(self, encounter, attackName, attackType, attackDamage, numberOfAttacks, multiplier):
    AttackMethods.choose_target(self, encounter)
    Draw.attack()
    damage = attackDamage * multiplier // 1
    for n in range(numberOfAttacks):
      PrintText.Print_with_delay(f"You attempt to attack {self.target.name} with {attackName}!\n")
      self.target.damage_taken(damage, attackType)
  
  def random_targets_attack(self, encounter, attackName, attackType, attackDamage, numberOfAttacks, multiplier):
    Draw.attack()
    damage = attackDamage * multiplier // 1
    for n in range(numberOfAttacks):
      AttackMethods.random_target(self, encounter)
      PrintText.Print_with_delay(f"You attempt to attack {self.target.name} with {attackName}!\n")
      self.target.damage_taken(damage, attackType)

  def random_secondary_target_attack(self, encounter, attackName, attackType, attackDamage, numberOfAttacks, primaryMultiplier, secondaryMultiplier):
    AttackMethods.choose_target(self, encounter)
    Draw.attack()
    damage = attackDamage * primaryMultiplier // 1
    splashDamage = attackDamage * secondaryMultiplier // 1
    for n in range(numberOfAttacks):
      PrintText.Print_with_delay(f"You attempt to attack {self.target.name} with {attackName}!\n")
      self.target.damage_taken(damage, attackType)
      if len(encounter) > 1:
        AttackMethods.random_secondary_target(self, encounter)
        self.secondaryTarget.damage_taken(splashDamage, attackType)

  def all_target_attack(self, encounter, attackName, attackType, attackDamage, numberOfAttacks, primaryMultiplier, secondaryMultiplier):
    AttackMethods.choose_target(self, encounter)
    Draw.attack()
    damage = attackDamage * primaryMultiplier // 1
    splashDamage = attackDamage * secondaryMultiplier // 1
    for n in range(numberOfAttacks):
      PrintText.Print_with_delay(f"You attempt to attack {self.target.name} with {attackName}!\n")
      self.target.damage_taken(damage, attackType)
      for enemy in encounter:
        if enemy is not self.target:
          enemy.damage_taken(splashDamage, attackType)

class BasicAttack:
  def __init__(self):
    self.attackName = "Basic Attack"
    self.attackType = "physical"
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.attackName, self.attackType, attackPower, 1, 1)

class BasicMagicAttack:
  def __init__(self):
    self.attackName = "Basic Magic Attack"
    self.attackType = "magical"
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.single_target_attack(self, encounter, self.attackName, self.attackType, attackPower, 1, 1)

class Cleave:
  def __init__(self):
    self.attackName = "Cleave"
    self.attackType = "physical"

  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.random_secondary_target_attack(self, encounter, self.attackName, self.attackType, attackPower, 1, 0.8, 0.5)

class RapidStrikes:
  def __init__(self):
    self.attackName = "Rapid Strikes"
    self.attackType = "physical"
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.attackName, self.attackType, attackPower, 3, 0.8)

class ChaoticMagic:
  def __init__(self):
    self.attackName = "Chaotic Magic"
    self.attackType = "magical"
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.random_targets_attack(self, encounter, self.attackName, self.attackType, attackPower, 5, 0.6)

class Explosion:
  def __init__(self):
    self.attackName = "Explosion"
    self.attackType = "magical"
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.attackName, self.attackType, attackPower, 1, 1.5, 0.75)