import ascii_art
from enemies import Enemy
from character import NewPlayerCharacter as Character
from print_delay import PrintText
from random import choice

art = ascii_art.Draw()

class Fight:
  def __init__(self) -> None:
    pass
  
  def battle(enemy: Enemy, player: Character):
    while enemy:
      PrintText.Print_with_delay(f"You have {player.health}/{player.maxHealth} health points.\n")
      PrintText.Print_with_delay(f"You have {player.magic}/{player.maxMagic} magic points.\n")
      PrintText.Print_with_delay("Actions:\n  'a' - physical attack\n  'm' - magical attack\n  'i' - inspect enemy\n  'r' - run away\n")
      userInputAction = input("What do you do? -> ")

      if userInputAction == "a":
        art.attack()
        damage = player.strength
        PrintText.Print_with_delay(f"You attempt to attack {enemy.name} with a physical attack!\n")
        enemy.damage_taken(damage, "physical")

      elif userInputAction == "m" and player.magic > 0:
        art.attack()
        damage = player.intellect
        PrintText.Print_with_delay(f"You attempt to attack {enemy.name} with a magical attack!\n")
        enemy.damage_taken(damage, "magical")
        player.magic -= 1

      elif userInputAction == "i":
        art.inspect_enemy()
        enemy.display_stats()

      elif userInputAction == "r":
        art.escape()
        PrintText.Print_with_delay(f"You ran away from {enemy.name}\n")
        break

      else:
        PrintText.Print_with_delay("That's not a valid action\n")

      if enemy.health <= 0:
        art.victory()
        PrintText.Print_with_delay(f"{enemy.name} has been vanquished!\n")
        PrintText.Print_with_delay(f"You gain {enemy.experience} experience points and 1 Job Skill Point!\n")
        player.experience += enemy.experience
        player.job.skillPoints += 1

        while player.experienceNeeded <= player.experience:
          art.level_up()
          player.level_up()

        while player.job.skillPointsNeeded <= player.job.skillPoints:
          art.skill_up()
          player.job.skill_up()
          PrintText.Print_with_delay(f"{player.job.name} skill level is now level {player.job.skillLevel}\n")
          if player.job.skillLevel == 5 and player.job.unlockableJobs and (list(player.job.unlockableJobs.keys())[0] not in player.unlockedJobs.keys()):
            art.job_unlock()
            for jobName, jobObject in player.job.unlockableJobs.items():
              player.unlock_job(jobObject, jobName)
              PrintText.Print_with_delay(f"{jobName} unlocked!\n")
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
      
      PrintText.Print_with_delay(f"{enemy.name} attacks you with a {attackType} attack!\n")
      player.damage_taken(damage, attackType)

      if player.health <= 0:
        art.defeat()
        PrintText.Print_with_delay(f"{player.name} has been defeated! Oh no!\n")
        break