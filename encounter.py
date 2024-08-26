from random import choice

class Fight:
  def __init__(self) -> None:
    pass
  
  def battle(enemy, player):
    while enemy:
      print("Actions:\n  'a' - physical attack\n  'm' - magical attack\n  'i' - inspect enemy\n  'r' - run away")
      userInputAction = input("What do you do? -> ")

      if userInputAction == "a":
        damage = player.strength
        print(f"You attempt to attack {enemy.name} with a physical attack!")
        enemy.damage_taken(damage, "physical")

      elif userInputAction == "m":
        damage = player.intellect
        print(f"You attempt to attack {enemy.name} with a magical attack!")
        enemy.damage_taken(damage, "magical")

      elif userInputAction == "i":
        enemy.display_stats()

      elif userInputAction == "r":
        print(f"You run away from {enemy.name}")
        break

      else:
        print("That's not a valid action")

      if enemy.health <= 0:
        print(f"{enemy.name} has been vanquished!")
        print(f"You gain {enemy.experience} experience points!")
        player.experience += enemy.experience

        while player.experienceNeeded <= player.experience:
          player.level_up()

          if player.job == "Novice" and player.level == 5:
            player.class_change()
        break
      
      damage = enemy.strength
      attackType = "physical"
      if enemy.strength and enemy.intellect:
        attackType = choice(["physical", "magical"])
      if attackType == "magical":
        damage = enemy.intellect
      
      player.damage_taken(damage, attackType)
      print(f"{enemy.name} attacks you with a {attackType} attack!\nYou take {damage} points of damage!")

      if player.health <= 0:
        print(f"{player.name} has been defeated! Oh no!")
        break