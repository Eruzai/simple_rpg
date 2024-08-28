import ascii_art
from random import choice

art = ascii_art.Draw()

class Fight:
  def __init__(self) -> None:
    pass
  
  def battle(enemy, player):
    while enemy:
      print(f"You have {player.health}/{player.maxHealth} health points.")
      print(f"You have {player.magic}/{player.maxMagic} magic points.\n")
      print("Actions:\n  'a' - physical attack\n  'm' - magical attack\n  'i' - inspect enemy\n  'r' - run away")
      userInputAction = input("What do you do? -> ")

      if userInputAction == "a":
        art.attack()
        damage = player.strength
        print(f"You attempt to attack {enemy.name} with a physical attack!")
        enemy.damage_taken(damage, "physical")

      elif userInputAction == "m" and player.magic > 0:
        art.attack()
        damage = player.intellect
        print(f"You attempt to attack {enemy.name} with a magical attack!")
        enemy.damage_taken(damage, "magical")
        player.magic -= 1

      elif userInputAction == "i":
        art.inspect_enemy()
        enemy.display_stats()

      elif userInputAction == "r":
        art.escape()
        print(f"You ran away from {enemy.name}\n")
        break

      else:
        print("That's not a valid action")

      if enemy.health <= 0:
        art.victory()
        print(f"{enemy.name} has been vanquished!")
        print(f"You gain {enemy.experience} experience points!\n")
        player.experience += enemy.experience

        while player.experienceNeeded <= player.experience:
          art.level_up()
          player.level_up()

          if player.job == "Novice" and player.level == 5:
            art.job_unlock()
            player.class_change()
        break
      
      art.enemy_attack()
      damage = enemy.strength
      attackType = "physical"
      if enemy.strength == 0:
        damage = enemy.intellect
        attackType = "magical"
      if enemy.strength and enemy.intellect:
        attackType = choice(["physical", "magical"])
      if attackType == "magical":
        damage = enemy.intellect
      
      player.damage_taken(damage, attackType)
      print(f"{enemy.name} attacks you with a {attackType} attack!\nYou take {damage} points of damage!\n")

      if player.health <= 0:
        art.defeat()
        print(f"{player.name} has been defeated! Oh no!\n")
        break