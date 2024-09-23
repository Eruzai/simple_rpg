import enemy_abilities
from ascii_art import Draw
from print_delay import PrintText
from random import randint, choice

class Enemy:
  def __init__(self):
    self.name = None
    self.level = 0
    self.experience = 0
    self.health = 0
    self.strength = 0
    self.intellect = 0
    self.physicalDef = 0
    self.magicDef = 0
    self.abilities = [enemy_abilities.BasicAttack()]
    self.abilityChanceArray = [0]
    self.statusEffects = []

  def apply_status_effect(self, effect):
    effectExists = next((statusEffect for statusEffect in self.statusEffects if statusEffect.name == effect.name), None)
    if effectExists:
      effectExists.counter = effect.counter
    else:
      self.statusEffects.append(effect)
      effect.execute(self)

  def clear_status_effect(self, effect):
    index = next((i for i, statusEffect in enumerate(self.statusEffects) if statusEffect.name == effect.name), -1)
    effect.cancel_effect(self)
    del self.statusEffects[index]

  def damage_taken(self, basedamage, attackType):
    damage = basedamage * choice([0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.5]) // 1
    multiplier = 0
    if attackType == "physical":
      multiplier = self.physicalDef / 100
    elif attackType == "magical":
      multiplier = self.magicDef / 100
    damage -= basedamage * multiplier // 1
    self.health -= damage
    PrintText.Print_with_delay(f"{self.name} takes {damage} points of {attackType} damage!\n")
  
  def display_stats(self):
    PrintText.Print_with_delay(f"You reveal {self.name}'s secrets!\n")
    PrintText.Print_with_delay(f"Level: {self.level}\n")
    PrintText.Print_with_delay(f"Health: {self.health}\n")
    PrintText.Print_with_delay(f"Strength: {self.strength}\n")
    PrintText.Print_with_delay(f"Intellect: {self.intellect}\n")
    if hasattr(self, 'physicalDef'):
      PrintText.Print_with_delay(f"Physical Defense: {self.physicalDef}\n")
    if hasattr(self, 'magicDef'):
      PrintText.Print_with_delay(f"Magic Defense: {self.magicDef}\n")
    print("")

class Rat(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rat"
    self.level = randint(1, 2)
    self.health = 2
    self.strength = 1
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.Nibble(), enemy_abilities.Bite()]
    self.abilityChanceArray = [0, 0, 1, 1, 2]
    for _ in range(self.level):
      self.experience += 2
      self.health += randint(1, 2)
      self.strength += randint(1, 2)
  
  def draw(self):
    Draw.rat()

class RabidDog(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Rabid Dog"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.Bite(), enemy_abilities.Howl()]
    self.abilityChanceArray = [0, 0, 1, 1, 2]
    self.level = randint(1, 3)
    self.experience = 8
    self.health = 4
    self.strength = 3
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(2, 4)
      self.strength += randint(1, 2)
  
  def draw(self):
    Draw.rabid_dog()

class TinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Tiny Slime"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.Absorb(), enemy_abilities.Divide()]
    self.abilityChanceArray = [0, 0, 1, 1, 2]
    self.level = randint(1, 3)
    self.experience = 5
    self.health = 8
    self.strength = 2
    self.physicalDef = 10
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(3, 5)
      self.strength += randint(1, 2)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.tiny_slime()

class MysteriousShadow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Mysterious Shadow"
    self.level = 20
    self.experience = 100000
    self.health = 500
    self.strength = 100
    self.intellect = 100
    self.physicalDef = 50
    self.magicDef = 50

  def draw(self):
    Draw.mysterious_shadow()

class SmallSlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Slime"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.Absorb(), enemy_abilities.Divide()]
    self.abilityChanceArray = [0, 0, 1, 1, 2]
    self.level = randint(1, 3)
    self.experience = 10
    self.health = 10
    self.strength = 3
    self.physicalDef = 15
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(3, 5)
      self.strength += randint(1, 2)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.small_slime()

class Slime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Slime"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.Absorb(), enemy_abilities.Divide()]
    self.abilityChanceArray = [0, 0, 1, 1, 2]
    self.level = randint(1, 5)
    self.experience = 15
    self.health = 12
    self.strength = 4
    self.physicalDef = 20
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(4, 6)
      self.strength += randint(1, 3)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.slime()

class Goblin(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Goblin"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.DoubleSlash(), enemy_abilities.GoblinDance()]
    self.abilityChanceArray = [0, 1, 2]
    self.level = randint(3, 5)
    self.experience = 15
    self.health = 8
    self.strength = 4
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(2, 4)
      self.strength += randint(2, 4)

  def draw(self):
    Draw.goblin()

class SmallSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Small Spider"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.CorrosiveBite(), enemy_abilities.InjectVenom()]
    self.abilityChanceArray = [0, 1, 2]
    self.level = randint(1, 3)
    self.experience = 12
    self.health = 12
    self.strength = 5
    for _ in range(self.level):
      self.experience += 3
      self.health += randint(2, 4)
      self.strength += randint(1, 3)

  def draw(self):
    Draw.small_spider()

class WindElemental(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Wind Elemental"
    self.abilities = [enemy_abilities.BasicMagicAttack(), enemy_abilities.WindSlash(), enemy_abilities.WindStorm()]
    self.abilityChanceArray = [0, 1, 2, 2]
    self.level = randint(3, 5)
    self.experience = 20
    self.health = 15
    self.intellect = 5
    self.physicalDef = 35
    for _ in range(self.level):
      self.experience += 4
      self.health += randint(3, 5)
      self.intellect += randint(2, 4)
      self.physicalDef += randint(3, 7)

  def draw(self):
    Draw.wind_elemental()

class ShinySlime(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Shiny Slime"
    self.abilities = [enemy_abilities.BasicAttack(), enemy_abilities.BasicMagicAttack(), enemy_abilities.Dissolve(), enemy_abilities.AcidSplash(), enemy_abilities.RapidDivision()]
    self.abilityChanceArray = [0, 1, 2, 3, 4]
    self.level = randint(5, 7)
    self.experience = 50
    self.health = 20
    self.strength = 5
    self.intellect = 5
    self.physicalDef = 35
    self.magicDef = 35
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(4, 7)
      self.strength += randint(4, 7)
      self.intellect += randint(4, 7)
      self.physicalDef += randint(1, 3)
      self.magicDef += randint(1, 3)

  def draw(self):
    Draw.shiny_slime()

class MarshSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Marsh Spider"
    self.level = randint(5, 8)
    self.experience = 25
    self.health = 12
    self.strength = 5
    self.physicalDef = 15
    for _ in range(self.level):
      self.experience += 6
      self.health += randint(2, 4)
      self.strength += randint(1, 3)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.marsh_spider()

class Zombie(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Zombie"
    self.level = randint(5, 8)
    self.experience = 30
    self.health = 15
    self.strength = 3
    self.physicalDef = 15
    for _ in range(self.level):
      self.experience += 6
      self.health += randint(3, 5)
      self.strength += randint(1, 2)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.zombie()

class GiantRat(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Giant Rat"
    self.level = randint(5, 8)
    self.experience = 25
    self.health = 8
    self.strength = 6
    for _ in range(self.level):
      self.experience += 6
      self.health += randint(1, 3)
      self.strength += randint(2, 3)

  def draw(self):
    Draw.giant_rat()

class DarkSerpent(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Dark Serpent"
    self.level = randint(6, 9)
    self.experience = 40
    self.health = 10
    self.strength = 5
    for _ in range(self.level):
      self.experience += 8
      self.health += randint(1, 3)
      self.strength += randint(2, 4)

  def draw(self):
    Draw.dark_serpent()

class Witch(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Witch"
    self.level = randint(7, 10)
    self.experience = 75
    self.health = 15
    self.strength = 5
    self.intellect = 10
    self.magicDef = 30
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(3, 5)
      self.strength += randint(1, 3)
      self.intellect += randint(3, 6)
      self.magicDef += randint(3, 5)

  def draw(self):
    Draw.witch()

class WretchedCrow(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "WretchedCrow"
    self.level = randint(6, 8)
    self.experience = 75
    self.health = 10
    self.strength = 4
    self.physicalDef = 40
    for _ in range(self.level):
      self.experience += 5
      self.health += randint(2, 4)
      self.strength += randint(2, 3)
      self.physicalDef += randint(3, 5)

  def draw(self):
    Draw.wretched_crow()

class MarshHorror(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Marsh Horror"
    self.level = randint(10, 12)
    self.experience = 400
    self.health = 50
    self.strength = 5
    self.intellect = 2
    self.physicalDef = 40
    self.magicDef = 25
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(5, 8)
      self.strength += randint(2, 4)
      self.intellect += randint(1, 3)
      self.physicalDef += randint(2, 4)
      self.magicDef += randint(2, 4)

  def draw(self):
    Draw.marsh_horror()

class WalkingArmor(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Walking Armor"
    self.level = randint(11, 15)
    self.experience = 100
    self.health = 25
    self.strength = 8
    self.physicalDef = 30
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(3, 6)
      self.strength += randint(2, 4)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.walking_armor()

class StoneSpider(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Stone Spider"
    self.level = randint(11, 15)
    self.experience = 100
    self.health = 15
    self.physicalDef = 20
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(3, 5)
      self.strength += randint(1, 3)
      self.physicalDef += randint(1, 3)

  def draw(self):
    Draw.stone_spider()

class AncientSpectre(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Ancient Spectre"
    self.level = randint(11, 15)
    self.experience = 115
    self.health = 10
    self.strength = 3
    self.intellect = 5
    self.physicalDef = 15
    self.magicDef = 15
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(1, 5)
      self.strength += randint(1, 3)
      self.intellect += randint(2, 4)
      self.physicalDef += randint(1, 3)
      self.magicDef += randint(2, 4)

  def draw(self):
    Draw.ancient_spectre()

class ColumnWyrm(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Column Wyrm"
    self.level = randint(11, 15)
    self.experience = 130
    self.health = 20
    self.strength = 6
    self.intellect = 2
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(3, 5)
      self.strength += randint(2, 4)
      self.intellect += randint(1, 2)

  def draw(self):
    Draw.column_wyrm()

class ShadowyCaster(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Shadowy Caster"
    self.level = randint(11, 15)
    self.experience = 130
    self.health = 10
    self.strength = 2
    self.intellect = 6
    self.physicalDef = 10
    self.magicDef = 25
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(1, 2)
      self.strength += randint(1, 2)
      self.intellect += randint(2, 4)
      self.physicalDef += randint(1, 2)
      self.magicDef += randint(2, 4)

  def draw(self):
    Draw.shadowy_caster()

class DancingBlades(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Dancing Blades"
    self.level = randint(11, 15)
    self.experience = 150
    self.health = 5
    self.strength = 10
    self.physicalDef = 25
    for _ in range(self.level):
      self.experience += 10
      self.health += randint(1, 2)
      self.strength += randint(3, 6)
      self.physicalDef += randint(2, 4)

  def draw(self):
    Draw.dancing_blades()

class VoidBeast(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "Void Beast"
    self.level = randint(11, 15)
    self.experience = 175
    self.health = 25
    self.strength = 6
    self.intellect = 10
    for _ in range(self.level):
      self.experience += 15
      self.health += randint(3, 6)
      self.strength += randint(1, 4)
      self.intellect += randint(1, 7)

  def draw(self):
    Draw.void_beast()

class TheEnd(Enemy):
  def __init__(self):
    super().__init__()
    self.name = "The End"
    self.level = 17
    self.experience = 2000
    self.health = 500
    self.strength = 75
    self.intellect = 75
    self.physicalDef = 30
    self.magicDef = 30

  def draw(self):
    Draw.the_end()
