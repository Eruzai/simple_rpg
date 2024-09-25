from print_delay import PrintText

class StatusEffect:
  def __init__(self):
    self.counter = 0
    self.name = None
    self.repeating = False
    self.firstApplication = True

  def count_down(self, target):
    self.counter -= 1
    if self.repeating:
      self.execute(target)
    if self.counter <= 0:
      target.clear_status_effect(self)

class DamageOverTime(StatusEffect):
  def __init__(self, name, activeTurns, damage):
    super().__init__()
    self.name = name
    self.counter = activeTurns
    self.repeating = True
    self.damage = damage

  def execute(self, target):
    target.health -= self.damage
    PrintText.Print_with_delay(f"{target.name} suffers {self.damage} damage from {self.name}\n")

  def cancel_effect(self, target):
    self.repeating = False

class StatAlteration(StatusEffect):
  def __init__(self, name, activeTurns, statToAdjust, adjustAmount):
    super().__init__()
    self.name = name
    self.counter = activeTurns
    self.statName = statToAdjust
    self.adjust = adjustAmount
    if self.adjust <= 0:
      self.message = "has decreased"
    else:
      self.message = "has increased"

  def execute(self, target):
    attribute = getattr(target, self.statName)
    setattr(target, self.statName, attribute + self.adjust)
    newAttribute = getattr(target, self.statName)
    if newAttribute < 0:
      self.adjust -= newAttribute
      setattr(target, self.statName, 0)
    if self.firstApplication:
      PrintText.Print_with_delay(f"{target.name} {self.message} {self.statName}!\n")

  def cancel_effect(self, target):
    attribute = getattr(target, self.statName)
    setattr(target, self.statName, attribute - self.adjust)
