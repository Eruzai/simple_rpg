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

  def choose_ability(encounter, player):
    abilities = []
    for abilityName, abilityObject in player.abilities.items():
      abilities.append(abilityName)
      print(f"  {len(abilities)} - {abilityName} - {abilityObject.abilityCost} AP cost")
    userInputAbility = int(input("Choose an ability -> ")) - 1
    chosenAbility = player.abilities[abilities[userInputAbility]]
    if chosenAbility.abilityCost > player.abilityPoints:
      PrintText.Print_with_delay("You don't have enough ability points to use that\n")
      Fight.choose_ability(encounter, player)
    else:
      player.abilities[abilities[userInputAbility]].execute(encounter, player)
    
  def battle(self, encounter: Enemy, player: Character):
    while encounter and player.health > 0:
      PrintText.Print_with_delay(f"You have {player.health}/{player.maxHealth} HP.\n")
      PrintText.Print_with_delay(f"You have {player.abilityPoints}/{player.maxAbilityPoints} AP.\n\n")
      print("Actions:\n  1 - fight\n  2 - inspect enemy\n  3 - run away\n")
      userInputAction = input("What do you do? -> ")
      ConsoleCommands.clear_console()

      if userInputAction == "1":
        Fight.choose_ability(encounter, player)

      elif userInputAction == "2":
        Draw.inspect_enemy()
        for enemy in encounter:
          enemy.display_stats()

      elif userInputAction == "3":
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
          player.job.skill_up(player)
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
