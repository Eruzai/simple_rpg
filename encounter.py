from ascii_art import Draw
from enemies import Enemy as Foes
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

  def player_defeated(self, player):
    if player.health <= 0:
      Draw.defeat()
      PrintText.Print_with_delay(f"{player.name} has been defeated! Your adventure has ended!\n")
      return True
    
  def handle_defeated_enemies(self, encounter):
    for index in range(len(encounter) -1, -1, -1):
      enemy = encounter[index]
      if enemy.health <= 0:
        PrintText.Print_with_delay(f"{enemy.name} has been defeated!\n")
        self.experienceEarned += enemy.experience
        self.jobPointsEarned += 1
        del encounter[index]

  def all_enemies_defeated(self, encounter, player):
    if len(encounter) == 0:
      Draw.victory()
      PrintText.Print_with_delay("All enemies have been defeated!\n")
      PrintText.Print_with_delay(f"You gain {self.experienceEarned} experience points and {self.jobPointsEarned} Job Skill Points!\n")
      player.experience += self.experienceEarned
      player.job.skillPoints += self.jobPointsEarned
      while player.experienceNeeded <= player.experience:
        Draw.level_up()
        player.level_up()
      while player.job.skillPointsNeeded <= player.job.skillPoints:
        Draw.skill_up()
        player.job.skill_up(player)
      return True

  def choose_ability(self, encounter, player):
    abilities = []

    for abilityName, abilityObject in player.abilities.items():
      abilities.append(abilityName)
      print(f"  {len(abilities)} - {abilityName} - {abilityObject.abilityCost} AP cost")

    PrintText.Print_with_delay(f"You have {player.abilityPoints}/{player.maxAbilityPoints} AP\n")
    userInputAbility = int(input("Choose an ability -> ")) - 1
    chosenAbility = player.abilities[abilities[userInputAbility]]

    if chosenAbility.abilityCost > player.abilityPoints:
      PrintText.Print_with_delay("You don't have enough ability points to use that\n")
      self.choose_ability(encounter, player)
    else:
      player.abilities[abilities[userInputAbility]].execute(encounter, player)

  def choose_action(self, encounter, player):
    print("Actions:\n  1 - Fight\n  2 - Inspect enemies\n  3 - Run away\n")
    userInputAction = input("What do you do? -> ")
    ConsoleCommands.clear_console()

    if userInputAction == "1":
      self.choose_ability(encounter, player)
    elif userInputAction == "2":
      Draw.inspect_enemy()
      for enemy in encounter:
        enemy.display_stats()
    elif userInputAction == "3":
      Draw.escape()
      PrintText.Print_with_delay(f"You escaped!\n")
      for index in range(len(player.statusEffects) -1, -1, -1):
        player.clear_status_effect[index]
      encounter = None
      return False
    else:
      PrintText.Print_with_delay("That's not a valid action\n")
      self.choose_action(encounter, player)
    
  def battle(self, encounter: Foes, player: Character):
    while encounter and player.health > 0:
      PrintText.Print_with_delay(f"You have {player.health}/{player.maxHealth} HP.\n")
      PrintText.Print_with_delay(f"You have {player.abilityPoints}/{player.maxAbilityPoints} AP.\n\n")

      if self.choose_action(encounter, player) is False:
        break

      self.handle_defeated_enemies(encounter)

      if self.all_enemies_defeated(encounter, player):
        break

      for index in range(len(player.statusEffects) -1, -1, -1):
        player.statusEffects[index].count_down(player)
        if self.player_defeated(player):
          break
      
      Draw.enemy_attack()
      for index in range(len(encounter) -1, -1, -1):
        enemy = encounter[index]
        enemyAbility = enemy.abilities[choice(enemy.abilityChanceArray)]
        PrintText.Print_with_delay(f"{enemy.name} uses {enemyAbility.name}!\n")
        enemyAbility.execute(player, enemy, encounter)

        if self.player_defeated(player):
          break

        for index in range(len(enemy.statusEffects) -1, -1, -1):
          enemy.statusEffects[index].count_down(enemy)

        self.handle_defeated_enemies(encounter)

        if self.all_enemies_defeated(encounter, player):
          break
