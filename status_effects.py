from print_delay import PrintText

class StatusEffect:
  def __init__(self):
    self.counter = 0
    self.name = None
    self.repeating = False

  def count_down(self, target):
    self.counter -= 1
    if self.repeating:
      self.execute(target)
    if self.counter <= 0:
      target.clear_status_effect(self)

class Poison(StatusEffect):
  def __init__(self, activeTurns):
    super().__init__()
    self.counter = activeTurns
    self.name = "Poison"
    self.repeating = True

  def execute(self, target):
    damage = target.health * 0.05 // 1
    target.health -= damage
    PrintText.Print_with_delay(f"{target.name} suffers {damage} poison damage")

  def cancel_effect(self, target):
    PrintText.Print_with_delay(f"{target.name} is no longer poisoned!")