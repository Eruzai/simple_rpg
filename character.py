import jobs
from print_delay import PrintText
from equipment import Item
from random import randint, choice

class NewPlayerCharacter:
  def __init__(self, name):
    self.name = name
    self.unlockedJobs = {"Novice": jobs.Novice()}
    self.job = self.unlockedJobs["Novice"]
    self.level = 1
    self.experience = 0
    self.experienceNeeded = 100
    self.baseMaxHealth = randint(40, 60)
    self.baseMaxMagic = randint(10, 15)
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
                                "maxMagic": 0,
                                "strength": 0,
                                "intellect": 0,
                                "physicalDef": 0,
                                "magicDef": 0}
    self.maxHealth = self.baseMaxHealth
    self.maxMagic = self.baseMaxMagic
    self.health = self.maxHealth
    self.magic = self.maxMagic
    self.strength = self.baseStrength
    self.intellect = self.baseIntellect
    self.physicalDef = 0
    self.magicDef = 0

  def calculate_stats(self):
    self.maxHealth = self.baseMaxHealth * self.job.healthMultiplier // 1 + self.totalEquipmentStats["maxHealth"]
    self.maxMagic = self.baseMaxMagic * self.job.magicMultiplier // 1 + self.totalEquipmentStats["maxMagic"]
    self.strength = self.baseStrength * self.job.strengthMultiplier // 1 + self.totalEquipmentStats["strength"]
    self.intellect = self.baseIntellect * self.job.intellectMultiplier // 1 + self.totalEquipmentStats["intellect"]
    self.physicalDef = self.basePhysicalDef + self.totalEquipmentStats["physicalDef"] + self.job.physicalDef
    self.magicDef = self.baseMagicDef + self.totalEquipmentStats["magicDef"] + self.job.magicDef
    if self.health > self.maxHealth:
      self.health = self.maxHealth
    if self.magic > self.maxMagic:
      self.magic = self.maxMagic

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
    PrintText.Print_with_delay(f"Magic: {self.magic}/{self.maxMagic}\n")
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

  def rest(self):
    self.health = self.maxHealth
    self.magic = self.maxMagic

  def unlock_job(self, jobObject, jobName):
    self.unlockedJobs[jobName] = jobObject()
  
  def switch_job(self, jobName):
    self.job = self.unlockedJobs[jobName]
    self.calculate_stats()
    self.display_stats()

  def level_up(self):
    self.level += 1
    self.experienceNeeded += 100 + self.experienceNeeded * 0.25 // 1
    self.baseMaxHealth += randint(5, 10)
    self.baseMaxMagic += randint(1, 3)
    self.baseHealth = self.maxHealth
    self.baseMagic = self.maxMagic
    self.baseStrength += randint(1, 3)
    self.baseIntellect += randint(1, 3)
    self.calculate_stats()
    self.rest()
    self.display_stats()
