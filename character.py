import jobs
import abilities
from print_delay import PrintText
from equipment import Item
from random import randint, choice

class NewPlayerCharacter:
  def __init__(self, name):
    self.name = name
    self.unlockedJobs = {"Novice": jobs.Novice()}
    self.job = self.unlockedJobs["Novice"]
    self.abilities = {"Attack": abilities.Attack(), "Magic Bolt": abilities.MagicBolt()}
    self.statusEffects = []
    self.level = 1
    self.experience = 0
    self.experienceNeeded = 100
    self.baseMaxHealth = randint(40, 60)
    self.baseMaxAbilityPoints = randint(10, 15)
    self.baseStrength = randint(10, 15)
    self.baseIntellect = randint(10, 15)
    self.basePhysicalDef = 0
    self.baseMagicDef = 0
    self.equipment = {"head": None,
                      "body": None,
                      "weapon": None,
                      "legs": None,
                      "feet": None,
                      "ring": None}
    self.totalEquipmentStats = {"maxHealth": 0,
                                "maxAbilityPoints": 0,
                                "strength": 0,
                                "intellect": 0,
                                "physicalDef": 0,
                                "magicDef": 0}
    self.maxHealth = self.baseMaxHealth
    self.maxAbilityPoints = self.baseMaxAbilityPoints
    self.health = self.maxHealth
    self.abilityPoints = self.maxAbilityPoints
    self.strength = self.baseStrength
    self.intellect = self.baseIntellect
    self.physicalDef = 0
    self.magicDef = 0

  def calculate_stats(self):
    self.maxHealth = self.baseMaxHealth * self.job.healthMultiplier // 1 + self.totalEquipmentStats["maxHealth"]
    self.maxAbilityPoints = self.baseMaxAbilityPoints * self.job.abilityPointsMultiplier // 1 + self.totalEquipmentStats["maxAbilityPoints"]
    self.strength = self.baseStrength * self.job.strengthMultiplier // 1 + self.totalEquipmentStats["strength"]
    self.intellect = self.baseIntellect * self.job.intellectMultiplier // 1 + self.totalEquipmentStats["intellect"]
    self.physicalDef = self.basePhysicalDef + self.totalEquipmentStats["physicalDef"] + self.job.physicalDef
    self.magicDef = self.baseMagicDef + self.totalEquipmentStats["magicDef"] + self.job.magicDef
    if self.health > self.maxHealth:
      self.health = self.maxHealth
    if self.abilityPoints > self.maxAbilityPoints:
      self.abilityPoints = self.maxAbilityPoints

  def unequip_item(self, item: Item):
    slot = item.equipSlot
    self.equipment[slot] = None
    for stat, value in item.stats.items():
      self.totalEquipmentStats[stat] -= value
    self.calculate_stats()

  def equip_item(self, item: Item):
    slot = item.equipSlot
    itemEquipped = self.equipment[slot]
    if itemEquipped is not None:
      self.unequip_item(itemEquipped)
    self.equipment[slot] = item
    for stat, value in item.stats.items():
      self.totalEquipmentStats[stat] += value
    self.calculate_stats()
  
  def damage_taken(self, basedamage, attackType):
    damage = basedamage * choice([0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.15, 1.5]) // 1
    multiplier = 0
    if attackType == "physical":
      multiplier = self.physicalDef / 100  
    elif attackType == "magical":
      multiplier = self.magicDef / 100
    damage -= damage * multiplier // 1
    self.health -= damage
    PrintText.Print_with_delay(f"You take {damage} points of damage!\n")
    print("")

  def display_stats(self):
    PrintText.Print_with_delay(f"{self.name} the {self.job.name}'s stats!\n")
    PrintText.Print_with_delay(f"Level: {self.level}\n")
    PrintText.Print_with_delay(f"Experience to Next Level up: {self.experienceNeeded - self.experience}\n")
    PrintText.Print_with_delay(f"Job Level: {self.job.skillLevel}\n")
    PrintText.Print_with_delay(f"Job Points to Next Skill Level: {self.job.skillPointsNeeded - self.job.skillPoints}\n")
    PrintText.Print_with_delay(f"Health: {self.health}/{self.maxHealth}\n")
    PrintText.Print_with_delay(f"Ability Points: {self.abilityPoints}/{self.maxAbilityPoints}\n")
    PrintText.Print_with_delay(f"Strength: {self.strength}\n")
    PrintText.Print_with_delay(f"Intellect: {self.intellect}\n")
    PrintText.Print_with_delay(f"Physical Defense: {self.physicalDef}\n")
    PrintText.Print_with_delay(f"Magic Defense: {self.magicDef}\n")
  
  def display_equipment(self):
    PrintText.Print_with_delay(f"{self.name} the {self.job.name}'s equipment!\n")
    for slot, item in self.equipment.items():
      item_name = item.name if item is not None else "None"
      PrintText.Print_with_delay(f"{slot}: {item_name}\n")
    print("")
  
  def display_abilites(self):
    PrintText.Print_with_delay(f"{self.name} can use these abilites:\n")
    for ability in self.abilities:
      PrintText.Print_with_delay(f"  {ability}\n")

  def rest(self):
    self.health = self.maxHealth
    self.abilityPoints = self.maxAbilityPoints

  def unlock_job(self, jobObject, jobName):
    self.unlockedJobs[jobName] = jobObject()
  
  def remove_abilities(self, jobAbilities):
    for ability in jobAbilities:
      del self.abilities[ability]

  def add_abilities(self, jobAbilities):
    for abilityName, abilityObject in jobAbilities.items():
      self.abilities[abilityName] = abilityObject

  def switch_job(self, jobName):
    self.remove_abilities(self.job.unlockedAbilities)
    self.job = self.unlockedJobs[jobName]
    self.add_abilities(self.job.unlockedAbilities)
    self.calculate_stats()
    self.display_stats()
    self.display_abilites()

  def level_up(self):
    self.level += 1
    self.experienceNeeded += 100 + self.experienceNeeded * 0.25 // 1
    self.baseMaxHealth += randint(5, 10)
    self.baseMaxAbilityPoints += randint(1, 3)
    self.baseHealth = self.maxHealth
    self.baseAbilityPoints = self.maxAbilityPoints
    self.baseStrength += randint(1, 3)
    self.baseIntellect += randint(1, 3)
    self.calculate_stats()
    self.rest()
    self.display_stats()

  def apply_status_effect(self, effect):
    search = next(((i, statusEffect) for i, statusEffect in enumerate(self.statusEffects) if statusEffect.name == effect.name), (None, None))
    index, effectExists = search
    if effectExists:
      effect.counter += effectExists.counter
      effect.firstApplication = False
      effectExists.cancel_effect(self)
      del self.statusEffects[index]
      PrintText.Print_with_delay(f"{effect.name}'s active time has been increased!\n")
    self.statusEffects.append(effect)
    effect.execute(self)

  def clear_status_effect(self, effect):
    index = next((i for i, statusEffect in enumerate(self.statusEffects) if statusEffect.name == effect.name), -1)
    effect.cancel_effect(self)
    PrintText.Print_with_delay(f"{self.name} is no longer under the effects of {effect.name}!\n")
    del self.statusEffects[index]
