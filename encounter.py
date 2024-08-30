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
        player.job.skillLevel = 5

        while player.experienceNeeded <= player.experience:
          art.level_up()
          player.level_up()

        if player.job.skillLevel == 5 and player.job.unlockableJobs and (list(player.job.unlockableJobs.keys())[0] not in player.unlockedJobs.keys()):
          art.job_unlock()
          for jobName, jobObject in player.job.unlockableJobs.items():
            player.unlock_job(jobObject, jobName)
            print(f"{jobName} unlocked!\n")
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
      
      print(f"{enemy.name} attacks you with a {attackType} attack!\n")
      player.damage_taken(damage, attackType)

      if player.health <= 0:
        art.defeat()
        print(f"{player.name} has been defeated! Oh no!\n")
        break