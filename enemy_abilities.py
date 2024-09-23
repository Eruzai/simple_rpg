from random import randint, choice
import copy
from print_delay import PrintText

class Summon:
  def execute(encounter, enemyToSummon):
    encounter.append(enemyToSummon)
    PrintText.Print_with_delay(f"a lvl {enemyToSummon.level} {enemyToSummon.name} has joined the battle!\n")

class Divide:
  def __init__(self):
    self.name = "Divide"

  def execute(self, player, enemy, encounter):
    PrintText.Print_with_delay(f"{enemy.name} begins to divide and copy itself!\n")
    enemy.health = enemy.health // 2
    newEnemy = copy.deepcopy(enemy)
    encounter.append(newEnemy)
    PrintText.Print_with_delay(f"A copy of {enemy.name} joins the battle!\n")

class Consume:
  def __init__(self):
    self.name = "Consume"

  def execute(self, player, attackingEnemy, encounter):
    choices = []
    for index, enemy in enumerate(encounter):
      if enemy is not attackingEnemy:
        choices.append(index)
    targetIndex = choice(choices)
    target = encounter[targetIndex]
    attackingEnemy.health += target.health
    PrintText.Print_with_delay(f"{attackingEnemy.name} has consumed {target.name} to regain {target.health} hp!\n")
    del encounter[targetIndex]

class Flee:
  def __init__(self):
    self.name = "Flee"

  def execute(self, player, fleeingEnemy, encounter):
    for index, enemy in enumerate(encounter):
      if enemy is fleeingEnemy:
        PrintText.Print_with_delay(f"{enemy.name} has fled!\n")
        del encounter[index]
        break

class BasicAttack:
  def __init__(self):
    self.name = "Basic Attack"
    
  def execute(self, player, enemy, encounter):
    attackPower = enemy.strength
    player.damage_taken(attackPower, "physical")

class BasicMagicAttack:
  def __init__(self):
    self.name = "Basic Magic Attack"
    
  def execute(self, player, enemy, encounter):
    attackPower = enemy.intellect
    player.damage_taken(attackPower, "magical")

class Nibble:
  def __init__(self):
    self.name = "Nibble"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength * 0.6
    numberOfAttacks = randint(1, 3)
    for n in range(numberOfAttacks):
      player.damage_taken(damage, "physical")

class Bite:
  def __init__(self):
    self.name = "Bite"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength * 1.5
    player.damage_taken(damage, "physical")

class Howl:
  def __init__(self):
    self.name = "Howl"
    
  def execute(self, player, enemy, encounter):
    from enemies import RabidDog as foe
    Summon.execute(encounter, foe())

class Dissolve:
  def __init__(self):
    self.name = "Dissolve"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength * 1.5
    health = player.health
    player.damage_taken(damage, "physical")
    healthRestored = health - player.health
    PrintText.Print_with_delay(f"{enemy.name} regenerates {healthRestored} hp!\n")
    enemy.health += healthRestored

class RapidDivision:
  def __init__(self):
    self.name = "Rapid Division"
    
  def execute(self, player, enemy, encounter):
    from enemies import Slime as foe
    Summon.execute(encounter, foe())
    Summon.execute(encounter, foe())

class DoubleSlash:
  def __init__(self):
    self.name = "Double Slash"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength * 0.8
    numberOfAttacks = 2
    for n in range(numberOfAttacks):
      player.damage_taken(damage, "physical")

class Boost:
  def __init__(self):
    self.name = "Boost"

  def execute(self, player, enemy, encounter):
    enemy.strength += 5
    PrintText.Print_with_delay(f"{enemy.name}'s strength increases!\n")
    