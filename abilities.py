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
    self.abilityCost = 0
  
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
    player.abilityPoints -= self.abilityCost

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
    player.abilityPoints -= self.abilityCost

class DoubleStrike:
  def __init__(self):
    self.name = "Double Strike"
    self.numberOfAttacks = 2
    self.multiplier = 0.8
    self.abilityCost = 3
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

class QuickCast:
  def __init__(self):
    self.name = "Quick Cast"
    self.multiplier = 0.4
    self.abilityCost = 5

  def execute(self, encounter, player):
    attackPower = player.intellect
    numberOfAttacks = randint(2, 5)
    AttackMethods.random_targets_attack(self, encounter, self.name, "magical", attackPower, numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

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
    player.abilityPoints -= self.abilityCost

class FocusMagic:
  def __init__(self):
    self.name = "Focus Magic"
    self.multiplier = 0.8
    self.abilityCost = 7

  def execute(self, encounter, player):
    attackPower = player.intellect
    numberOfAttacks = randint(1, 3)
    AttackMethods.single_target_attack(self, encounter, self.name, "magical", attackPower, numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

class RapidStrikes:
  def __init__(self):
    self.name = "Rapid Strikes"
    self.multiplier = 0.4
    self.abilityCost = 5
  
  def execute(self, encounter, player):
    attackPower = player.strength
    numberOfAttacks = randint(2, 5)
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

class WildStrikes:
  def __init__(self):
    self.name = "Wild Strikes"
    self.multiplier = 0.3
    self.splashMultiplier = 0.15
    self.abilityCost = 5
  
  def execute(self, encounter, player):
    attackPower = player.strength
    numberOfAttacks = randint(2, 5)
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "physical", attackPower, numberOfAttacks, self.multiplier, self.splashMultiplier)
    player.abilityPoints -= self.abilityCost

class FocusStrike:
  def __init__(self):
    self.name = "Focus Strike"
    self.multiplier = 1.5
    self.numberOfAttacks = 1
    self.abilityCost = 7
  
  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

class ChaoticMagic:
  def __init__(self):
    self.name = "Chaotic Magic"
    self.multiplier = 0.3
    self.abilityCost = 7
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    numberOfAttacks = randint(3, 7)
    AttackMethods.random_targets_attack(self, encounter, self.name, "magical", attackPower, numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

class ArcaneBolt:
  def __init__(self):
    self.name = "Arcane Bolt"
    self.multiplier = 0.4
    self.splashMultiplier = 0.2
    self.numberOfAttacks = 3
    self.abilityCost = 10
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    player.abilityPoints -= self.abilityCost

class DarkBolt:
  def __init__(self):
    self.name = "Dark Bolt"
    self.multiplier = 2
    self.splashMultiplier = 0.6
    self.numberOfAttacks = 1
    self.abilityCost = 10
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    selfHarm = attackPower * 0.25 // 1
    PrintText.Print_with_delay(f"You recieve recoil damage!")
    player.damage_taken(selfHarm, "magical")
    player.abilityPoints -= self.abilityCost

class ArcaneFlood:
  def __init__(self):
    self.name = "Arcane Flood"
    self.multiplier = 0.5
    self.splashMultiplier = 0.5
    self.numberOfAttacks = 3
    self.abilityCost = 7
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    player.abilityPoints -= self.abilityCost

class Drain:
  def __init__(self):
    self.name = "Drain"
    self.multiplier = 0.5
    self.numberOfAttacks = 1
    self.abilityCost = 10
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier)
    healAmount = attackPower * choice([0.05, 0.075, 0.1, 0.125, 0.15]) * len(encounter) // 1
    PrintText.Print_with_delay(f"You steal {healAmount} health from enemies!")
    player.health += healAmount
    if player.health > player.maxHealth:
      player.health = player.maxHealth
    player.abilityPoints -= self.abilityCost

class Erase:
  def __init__(self):
    self.name = "Erase"
    self.multiplier = 5
    self.splashMultiplier = 5
    self.numberOfAttacks = 1
    self.abilityCost = 15
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.name, "magical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    player.abilityPoints -= self.abilityCost

class DoubleCleave:
  def __init__(self):
    self.name = "Double Cleave"
    self.multiplier = 1.2
    self.splashMultiplier = 0.6
    self.numberOfAttacks = 2
    self.abilityCost = 7

  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    player.abilityPoints -= self.abilityCost

class BladeDance:
  def __init__(self):
    self.name = "Blade Dance"
    self.multiplier = 0.4
    self.abilityCost = 10

  def execute(self, encounter, player):
    attackPower = player.strength
    numberOfAttacks = randint(3, 7)
    AttackMethods.random_targets_attack(self, encounter, self.name, "physical", attackPower, numberOfAttacks, self.multiplier)
    player.abilityPoints -= self.abilityCost

class InvigoratingShout:
  def __init__(self):
    self.name = "Invigorating Shout"
    self.multiplier = 0.2
    self.splashMultiplier = 0.2
    self.numberOfAttacks = 1
    self.abilityCost = 5
  
  def execute(self, encounter, player):
    attackPower = player.intellect
    AttackMethods.all_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    healAmount = attackPower * choice([0.05, 0.075, 0.1, 0.125, 0.15]) * len(encounter) // 1
    PrintText.Print_with_delay(f"You restore {healAmount} magic!")
    player.abilityPoints += healAmount
    if player.abilityPoints > player.maxMagic:
      player.abilityPoints = player.maxMagic

class FuriousCleave:
  def __init__(self):
    self.name = "Furious Cleave"
    self.multiplier = 2
    self.splashMultiplier = 1.5
    self.numberOfAttacks = 1
    self.abilityCost = 7

  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.random_secondary_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier, self.splashMultiplier)
    player.abilityPoints -= self.abilityCost

class EnragedFlurry:
  def __init__(self):
    self.name = "Enraged Flurry"
    self.multiplier = 0.5
    self.abilityCost = 10

  def execute(self, encounter, player):
    attackPower = player.strength
    numberOfAttacks = randint(5, 10)
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, numberOfAttacks, self.multiplier)
    selfHarm = attackPower * 0.05 * numberOfAttacks // 1
    PrintText.Print_with_delay(f"You recieve recoil damage!")
    player.damage_taken(selfHarm, "physical")
    player.abilityPoints -= self.abilityCost

class BerserkSlash:
  def __init__(self):
    self.name = "Berserk Slash"
    self.multiplier = 5
    self.numberOfAttacks = 1
    self.abilityCost = 15

  def execute(self, encounter, player):
    attackPower = player.strength
    AttackMethods.single_target_attack(self, encounter, self.name, "physical", attackPower, self.numberOfAttacks, self.multiplier)
    selfHarm = attackPower * 0.5 // 1
    PrintText.Print_with_delay(f"You recieve recoil damage!")
    player.damage_taken(selfHarm, "physical")
    player.abilityPoints -= self.abilityCost
