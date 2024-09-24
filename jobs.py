import abilities
from print_delay import PrintText
from ascii_art import Draw

class Job:
  def __init__(self):
    self.name = ""
    self.unlockableJobs = {}
    self.unlockedAbilities = {}
    self.unlockableAbilities = []
    self.skillLevel = 1
    self.skillPoints = 0
    self.skillPointsNeeded = 5

  def skill_up(self, player):
    self.skillLevel += 1
    self.skillPointsNeeded += 5 + self.skillPointsNeeded * 0.25 // 1
    PrintText.Print_with_delay(f"{self.name} skill level is now level {self.skillLevel}\n{self.skillPointsNeeded - self.skillPoints} points to next job level up!\n")
    if self.skillLevel == 3:
      self.unlock_ability(self.unlockableAbilities[0](), player)
    if self.skillLevel == 5:
      self.unlock_ability(self.unlockableAbilities[1](), player)
      if self.unlockableJobs:
        Draw.job_unlock()
        for jobName, jobObject in self.unlockableJobs.items():
          player.unlock_job(jobObject, jobName)
          PrintText.Print_with_delay(f"{jobName} unlocked!\n")

  def unlock_ability(self, ability, player):
    self.unlockedAbilities[ability.name] = ability
    player.abilities[ability.name] = ability
    PrintText.Print_with_delay(f"A new ability for {self.name}, {ability.name} unlocked!\n")

class Novice(Job):
  def __init__(self):
    super().__init__()
    self.name = "Novice"
    self.unlockableJobs = {"Magician": Magician, "Fighter": Fighter}
    self.unlockableAbilities = [abilities.LuckyStrike, abilities.DoubleStrike]
    self.healthMultiplier = 1
    self.abilityPointsMultiplier = 1
    self.strengthMultiplier = 1
    self.intellectMultiplier = 1
    self.physicalDef = 0
    self.magicDef = 0

class Magician(Job):
  def __init__(self):
    super().__init__()
    self.name = "Magician"
    self.unlockableJobs = {"Wizard": Wizard, "Sage": Sage}
    self.unlockedAbilities = {"Lucky Strike": abilities.LuckyStrike(), "Quick Cast": abilities.QuickCast()}
    self.unlockableAbilities = [abilities.MagicBlast, abilities.FocusMagic]
    self.healthMultiplier = 1.25
    self.abilityPointsMultiplier = 1.5
    self.strengthMultiplier = 1
    self.intellectMultiplier = 1.5
    self.physicalDef = 5
    self.magicDef = 15

class Fighter(Job):
  def __init__(self):
    super().__init__()
    self.name = "Fighter"
    self.unlockableJobs = {"Warrior": Warrior, "Berserker": Berserker}
    self.unlockedAbilities = {"Double Strike": abilities.DoubleStrike(), "Rapid Strikes": abilities.RapidStrikes()}
    self.unlockableAbilities = [abilities.WildStrikes, abilities.FocusStrike]
    self.healthMultiplier = 1.5
    self.abilityPointsMultiplier = 1
    self.strengthMultiplier = 1.5
    self.intellectMultiplier = 1
    self.physicalDef = 15
    self.magicDef = 5

class Wizard(Job):
  def __init__(self):
    super().__init__()
    self.name = "Wizard"
    self.unlockedAbilities = {"Lucky Strike": abilities.LuckyStrike(), "Quick Cast": abilities.QuickCast(), "Focus Magic": abilities.FocusMagic(), "Chaotic Magic": abilities.ChaoticMagic()}
    self.unlockableAbilities = [abilities.ArcaneBolt, abilities.DarkBolt]
    self.healthMultiplier = 1.5
    self.abilityPointsMultiplier = 2
    self.strengthMultiplier = 1.25
    self.intellectMultiplier = 2.25
    self.physicalDef = 15
    self.magicDef = 30

class Sage(Job):
  def __init__(self):
    super().__init__()
    self.name = "Sage"
    self.unlockedAbilities = {"Lucky Strike": abilities.LuckyStrike(), "Quick Cast": abilities.QuickCast(), "Magic Blast": abilities.MagicBlast(), "Arcane Flood": abilities.ArcaneFlood()}
    self.unlockableAbilities = [abilities.Drain, abilities.Erase]
    self.healthMultiplier = 1.75
    self.abilityPointsMultiplier = 2
    self.strengthMultiplier = 1.25
    self.intellectMultiplier = 2
    self.physicalDef = 10
    self.magicDef = 40

class Warrior(Job):
  def __init__(self):
    super().__init__()
    self.name = "Warrior"
    self.unlockedAbilities = {"Double Strike": abilities.DoubleStrike(), "Rabid Strikes": abilities.RapidStrikes(), "Wild Strikes": abilities.WildStrikes(), "Double Cleave": abilities.DoubleCleave()}
    self.unlockableAbilities = [abilities.BladeDance, abilities.InvigoratingShout]
    self.healthMultiplier = 2
    self.abilityPointsMultiplier = 1
    self.strengthMultiplier = 2.5
    self.intellectMultiplier = 1
    self.physicalDef = 25
    self.magicDef = 15

class Berserker(Job):
  def __init__(self):
    super().__init__()
    self.name = "Berserker"
    self.unlockedAbilities = {"Double Strike": abilities.DoubleStrike(), "Rabid Strikes": abilities.RapidStrikes(), "Focus Strike": abilities.FocusStrike(), "Furious Cleave": abilities.FuriousCleave()}
    self.unlockableAbilities = [abilities.EnragedFlurry, abilities.BerserkSlash]
    self.healthMultiplier = 2.5
    self.abilityPointsMultiplier = 1
    self.strengthMultiplier = 2
    self.intellectMultiplier = 0.5
    self.physicalDef = 35
    self.magicDef = 35
