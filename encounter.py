from ascii_art import Draw
from enemies import Enemy
from character import NewPlayerCharacter as Character
from print_delay import PrintText
from console import ConsoleCommands
from random import choice

class Fight:
  def __init__(self):
    self.target = None
    self.targetIndex = None
    self.experienceEarned = 0
    self.jobPointsEarned = 0
    
  def battle(self, encounter: Enemy, player: Character):
    while encounter and player.health > 0:
      PrintText.Print_with_delay(f"You have {player.health}/{player.maxHealth} health points.\n")
      PrintText.Print_with_delay(f"You have {player.magic}/{player.maxMagic} magic points.\n\n")
      print("Actions:\n  'f' - fight\n  'i' - inspect enemy\n  'r' - run away\n")
      userInputAction = input("What do you do? -> ")
      ConsoleCommands.clear_console()

      if userInputAction == "f":
        for abilityName in player.abilities:
          print(f"  {abilityName}")
        userInputAbility = input("Choose an ability -> ")
        player.abilities[userInputAbility].execute(encounter, player)

      elif userInputAction == "i":
        Draw.inspect_enemy()
        for enemy in encounter:
          enemy.display_stats()

      elif userInputAction == "r":
        Draw.escape()
        PrintText.Print_with_delay(f"You escaped!\n")
        break

      else:
        PrintText.Print_with_delay("That's not a valid action\n")
      
      for index in range(len(encounter) -1, -1, -1):
        enemy = encounter[index]
        if enemy.health <= 0:
          PrintText.Print_with_delay(f"{enemy.name} has been defeated!\n")
          self.experienceEarned += enemy.experience
          self.jobPointsEarned += 1
          del encounter[index]
          

      if len(encounter) == 0:
        Draw.victory()
        PrintText.Print_with_delay("All enemies have been vanquished!\n")
        PrintText.Print_with_delay(f"You gain {self.experienceEarned} experience points and {self.jobPointsEarned} Job Skill Points!\n")
        player.experience += self.experienceEarned
        player.job.skillPoints += self.jobPointsEarned

        while player.experienceNeeded <= player.experience:
          Draw.level_up()
          player.level_up()

        while player.job.skillPointsNeeded <= player.job.skillPoints:
          Draw.skill_up()
          player.job.skill_up()
          PrintText.Print_with_delay(f"{player.job.name} skill level is now level {player.job.skillLevel}\n")
          if player.job.skillLevel == 5 and player.job.unlockableJobs and (list(player.job.unlockableJobs.keys())[0] not in player.unlockedJobs.keys()):
            Draw.job_unlock()
            for jobName, jobObject in player.job.unlockableJobs.items():
              player.unlock_job(jobObject, jobName)
              PrintText.Print_with_delay(f"{jobName} unlocked!\n")
        break
      
      Draw.enemy_attack()
      for enemy in encounter:
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
          Draw.defeat()
          PrintText.Print_with_delay(f"{player.name} has been defeated! Your adventure has ended!\n")
