
class Fight:
  def __init__(self) -> None:
    pass
  
  def battle(enemy, player):
    while enemy and enemy.health > 0 and player.health > 0:
      print("Actions:\n  'a' - attack\n  'm' - magical attack\n  'i' - inspect enemy\n  'r' - run away")
      userInputAction = input("What do you do? -> ")

      if userInputAction == "a":
        damage = player.strength

        if hasattr(enemy, 'physicalDef'):
          enemyDefMultiplier = enemy.physicalDef / 100
          damage = player.strength - player.strength * enemyDefMultiplier // 1

        enemy.damage_taken(damage)
        print(f"You inflict {damage} points of physical damage to {enemy.name}")

      elif userInputAction == "m":
        damage = player.intellect

        if hasattr(enemy, 'magicDef'):
          enemyDefMultiplier = enemy.magicDef / 100
          damage = player.intellect - player.intellect * enemyDefMultiplier // 1

        enemy.damage_taken(damage)
        print(f"You inflict {damage} points of magical damage to {enemy.name}")

      elif userInputAction == "i":
        enemy.display_stats()

      elif userInputAction == "r":
        print(f"You run away from {enemy.name}")
        enemy = None

      else:
        print("That's not a valid action")