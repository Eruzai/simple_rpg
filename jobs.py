class Job:
  def __init__(self):
    self.unlockableJobs = None
    self.skillLevel = 1
    self.skillPoints = 0
    self.skillPointsNeeded = 5

  def skill_up(self):
    self.skillLevel += 1
    self.skillPointsNeeded += 5 + self.skillPointsNeeded * 0.25 // 1

class Novice(Job):
  def __init__(self):
    super().__init__()
    self.name = "Novice"
    self.unlockableJobs = {"Magician": Magician, "Fighter": Fighter}
    self.healthMultiplier = 1
    self.magicMultiplier = 1
    self.strengthMultiplier = 1
    self.intellectMultiplier = 1
    self.physicalDef = 0
    self.magicDef = 0

class Magician(Job):
  def __init__(self):
    super().__init__()
    self.name = "Magician"
    self.unlockableJobs = {"Wizard": Wizard, "Sage": Sage}
    self.healthMultiplier = 1.25
    self.magicMultiplier = 1.5
    self.strengthMultiplier = 1
    self.intellectMultiplier = 1.5
    self.physicalDef = 5
    self.magicDef = 15

class Fighter(Job):
  def __init__(self):
    super().__init__()
    self.name = "Fighter"
    self.unlockableJobs = {"Warrior": Warrior, "Berserker": Berserker}
    self.healthMultiplier = 1.5
    self.magicMultiplier = 1
    self.strengthMultiplier = 1.5
    self.intellectMultiplier = 1
    self.physicalDef = 15
    self.magicDef = 5

class Wizard(Job):
  def __init__(self):
    super().__init__()
    self.name = "Wizard"
    self.healthMultiplier = 1.5
    self.magicMultiplier = 2
    self.strengthMultiplier = 1.25
    self.intellectMultiplier = 2.25
    self.physicalDef = 15
    self.magicDef = 30

class Sage(Job):
  def __init__(self):
    super().__init__()
    self.name = "Sage"
    self.healthMultiplier = 1.75
    self.magicMultiplier = 2
    self.strengthMultiplier = 1.25
    self.intellectMultiplier = 2
    self.physicalDef = 10
    self.magicDef = 40

class Warrior(Job):
  def __init__(self):
    super().__init__()
    self.name = "Warrior"
    self.healthMultiplier = 2
    self.magicMultiplier = 1
    self.strengthMultiplier = 2.5
    self.intellectMultiplier = 1
    self.physicalDef = 25
    self.magicDef = 15

class Berserker(Job):
  def __init__(self):
    super().__init__()
    self.name = "Berserker"
    self.healthMultiplier = 2.5
    self.magicMultiplier = 1
    self.strengthMultiplier = 2
    self.intellectMultiplier = 0.5
    self.physicalDef = 35
    self.magicDef = 35
