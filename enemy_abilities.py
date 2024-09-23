from random import randint, choice
import copy
from print_delay import PrintText
import status_effects

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

class Absorb:
  def __init__(self):
    self.name = "Absorb"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength
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

class GoblinDance:
  def __init__(self):
    self.name = "Goblin Dance"

  def execute(self, player, enemy, encounter):
    effect = status_effects.StatAlteration(self.name, 3, "strength", 5)
    for enemy in encounter:
      enemy.apply_status_effect(effect)

class InjectVenom:
  def __init__(self):
    self.name = "Inject Venom"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength
    damageOverTime = player.maxHealth * 0.05 // 1
    player.damage_taken(damage, "physical")
    effect = status_effects.DamageOverTime(self.name, 3, damageOverTime)
    player.apply_status_effect(effect)

class CorrosiveBite:
  def __init__(self):
    self.name = "Corrosive Bite"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength
    adjustment = player.physicalDef * 0.5 // 1
    player.damage_taken(damage, "physical")
    effect = status_effects.StatAlteration(self.name, 3, "physicalDef", -adjustment)
    player.apply_status_effect(effect)

class WindStorm:
  def __init__(self):
    self.name = "Wind Storm"

  def execute(self, player, enemy, encounter):
    damage = enemy.intellect * 0.3
    numberOfAttacks = randint(2, 5)
    for n in range(numberOfAttacks):
      player.damage_taken(damage, "magical")
    adjustment = player.magicalDef * 0.5 // 1
    effect1 = status_effects.StatAlteration(self.name, 3, "magicalDef", -adjustment)
    effect2 = status_effects.StatAlteration(self.name, 3, "intellect", 5)
    player.apply_status_effect(effect1)
    enemy.apply_status_effect(effect2)

class WindSlash:
  def __init__(self):
    self.name = "Wind Slash"

  def execute(self, player, enemy, encounter):
    damage = enemy.intellect * 1.2
    player.damage_taken(damage, "magical")

class Dissolve:
  def __init__(self):
    self.name = "Dissolve"

  def execute(self, player, enemy, encounter):
    damage = enemy.strength
    health = player.health
    player.damage_taken(damage, "physical")
    healthRestored = health - player.health
    PrintText.Print_with_delay(f"{enemy.name} regenerates {healthRestored} hp!\n")
    enemy.health += healthRestored
    adjustment = player.physicalDef * 0.5 // 1
    effect1 = status_effects.StatAlteration(self.name, 5, "physicalDef", -adjustment)
    effect2 = status_effects.StatAlteration(self.name, 2, "physicalDef", 15)
    player.apply_status_effect(effect1)
    enemy.apply_status_effect(effect2)

class AcidSplash:
  def __init__(self):
    self.name = "Acid Splash"

  def execute(self, player, enemy, encounter):
    damage = enemy.intellect
    damageOverTime = player.maxHealth * 0.05 // 1
    player.damage_taken(damage, "magical")
    adjustment = player.magicalDef * 0.5 // 1
    effect = status_effects.StatAlterWithDOT(self.name, 3, damageOverTime, "magicalDef", -adjustment)
    player.apply_status_effect(effect)