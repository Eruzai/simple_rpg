from random import randint
import jobs

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
    self.head = None
    self.body = None
    self.weapon = None
    self.legs = None
    self.feet = None
    self.ring = None
    self.maxHealth = self.baseMaxHealth
    self.maxMagic = self.baseMaxMagic
    self.health = self.maxHealth
    self.magic = self.maxMagic
    self.strength = self.baseStrength
    self.intellect = self.baseIntellect
    self.physicalDef = 0
    self.magicDef = 0

  def calculate_stats(self):
    self.maxHealth = self.baseMaxHealth * self.job.healthMultiplier // 1
    self.maxMagic = self.baseMaxMagic * self.job.magicMultiplier // 1
    self.strength = self.baseStrength * self.job.strengthMultiplier // 1
    self.intellect = self.baseIntellect * self.job.intellectMultiplier // 1
    self.physicalDef = self.basePhysicalDef + self.job.physicalDef
    self.magicDef = self.baseMagicDef + self.job.magicDef
    if self.health > self.maxHealth:
      self.health = self.maxHealth
    if self.magic > self.maxMagic:
      self.magic = self.maxMagic
  
  def damage_taken(self, basedamage, attackType):
    damage = basedamage
    multiplier = 0
    if attackType == "physical":
      multiplier = self.physicalDef / 100  
    elif attackType == "magical":
      multiplier = self.magicDef / 100
    damage -= basedamage * multiplier // 1
    self.health -= damage
    print(f"You take {damage} points of damage!\n")

  def display_stats(self):
    print(f"{self.name} the {self.job.name}'s stats!")
    print(f"Level: {self.level}")
    print(f"Experience to next Level up: {self.experienceNeeded - self.experience}")
    print(f"Health: {self.health}/{self.maxHealth}")
    print(f"Magic: {self.magic}/{self.maxMagic}")
    print(f"Strength: {self.strength}")
    print(f"Intellect: {self.intellect}")
    print(f"Physical Defense: {self.physicalDef}")
    print(f"Magic Defense: {self.magicDef}\n")
  
  def display_equipment(self):
    print(f"{self.name} the {self.job.name}'s equipment!")
    print(f"Head: {self.head}")
    print(f"Body: {self.body}")
    print(f"Weapon: {self.weapon}")
    print(f"Legs: {self.legs}")
    print(f"Feet: {self.feet}")
    print(f"Ring: {self.ring}\n")

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
