import ascii_art
from enemies import Enemy
from character import NewPlayerCharacter as Character
from print_delay import PrintText
from console import ConsoleCommands
from random import choice

art = ascii_art.Draw()

class Fight:
  def __init__(self):
    self.target = None
    self.targetIndex = None
    self.experienceEarned = 0
    self.jobPointsEarned = 0

  def attack(self, attackType, encounter, player):
    if len(encounter) > 1:
      PrintText.Print_with_delay("Choose target:\n")
      for index, enemy in enumerate(encounter):
        print(f"  {index + 1} - {enemy.name}")
      self.targetIndex = int(input("enter number for target -> ")) - 1
      ConsoleCommands.clear_console()
      self.target = encounter[self.targetIndex]
    art.attack()
    damage = player.strength
    PrintText.Print_with_delay(f"You attempt to attack {self.target.name} with a {attackType} attack!\n")
    self.target.damage_taken(damage, attackType)
    
  def battle(self, encounter: Enemy, player: Character):
    while encounter:
      self.target = encounter[0]
      self.targetIndex = 0
      PrintText.Print_with_delay(f"You have {player.health}/{player.maxHealth} health points.\n")
      PrintText.Print_with_delay(f"You have {player.magic}/{player.maxMagic} magic points.\n\n")
      print("Actions:\n  'a' - physical attack\n  'm' - magical attack\n  'i' - inspect enemy\n  'r' - run away\n")
      userInputAction = input("What do you do? -> ")
      ConsoleCommands.clear_console()

      if userInputAction == "a":
        self.attack("physical", encounter, player)

      elif userInputAction == "m" and player.magic > 0:
        self.attack("magical", encounter, player)
        player.magic -= 1

      elif userInputAction == "i":
        art.inspect_enemy()
        for enemy in encounter:
          enemy.display_stats()

      elif userInputAction == "r":
        art.escape()
        PrintText.Print_with_delay(f"You escaped!\n")
        break

      else:
        PrintText.Print_with_delay("That's not a valid action\n")

      if self.target.health <= 0:
        PrintText.Print_with_delay(f"{self.target.name} has been defeated!\n")
        self.experienceEarned += self.target.experience
        self.jobPointsEarned += 1
        del encounter[self.targetIndex]

      if len(encounter) is 0:
        art.victory()
        PrintText.Print_with_delay("All enemies have been vanquished!\n")
        PrintText.Print_with_delay(f"You gain {self.experienceEarned} experience points and {self.jobPointsEarned} Job Skill Points!\n")
        player.experience += self.experienceEarned
        player.job.skillPoints += self.jobPointsEarned

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
          art.defeat()
          PrintText.Print_with_delay(f"{player.name} has been defeated! Your adventure has ended!\n")
          break