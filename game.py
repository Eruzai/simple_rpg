import game_state, character, locations, encounter, found_treasure
from ascii_art import Draw
from console import ConsoleCommands
from print_delay import PrintText

Draw.welcome()
Draw.title()

print("Actions:\n  'n' - start new game\n  'l' - load game\n")
userInputLoadGame = input("-> ")
ConsoleCommands.clear_console()

if userInputLoadGame == 'l':
  print("Save files:\n  '1' - file1\n  '2' - file2\n  '3' - file3\n")
  fileNumber = input("Choose save file -> ")
  ConsoleCommands.clear_console()
  fileLocation = f"file{fileNumber}"
  player = character.NewPlayerCharacter('noname')
  game_state.GameState.load_game(fileLocation, player)
elif userInputLoadGame == 'n':
  userInputName = input("Enter your character's name -> ")
  ConsoleCommands.clear_console()
  player = character.NewPlayerCharacter(userInputName)
  fileLocation = None

Draw.stat_heading()
player.display_stats()

Draw.welcome()
Draw.town_of_respite()
location = locations.TownOfRespite()

while player.health > 0:
  PrintText.Print_with_delay(f"You are walking around the {location.name}.\n")
  print("Actions:\n  1 - explore\n  2 - inspect stats and equipment\n  3 - leave")

  if location.name == "Town of Respite":
    print("  4 - rest at the inn and save game")
    if len(player.unlockedJobs) > 1:
      print("  5 - change job\n")
    print("  Q - quit game\n")

  userInputAction = input("What do you want to do? -> ")
  ConsoleCommands.clear_console()

  if userInputAction == "1":
    Draw.exploring()
    location.explore()

    if location.encounter:
      Draw.battle_notification()
      for enemy in location.encounter:
        PrintText.Print_with_delay(f"A level {enemy.level} {enemy.name}\n")
        enemy.draw()
      PrintText.Print_with_delay("Appears before you! Begin battle!\n")
      battle = encounter.Fight()
      battle.battle(location.encounter, player)
      location.encounter = None
    
    if location.treasure:
      PrintText.Print_with_delay(f"You've discovered a {location.treasure.name} lying on the ground!\n\n")
      found_treasure.Treasure.equip_item(location.treasure, player)
      location.treasure = None

  elif userInputAction == "3":
    Draw.open_map()
    PrintText.Print_with_delay("There are a few interesting locations nearby...\n")
    print("Locations:\n  1 - Town of Respite\n  2 - Fields of Beginning (levels 1 - 5)\n  3 - Middling Marrow (levels 6 - 10)\n  4 - Keep of the End (levels 11 - 15)\n")
    userInputLocation = input("Where would you like to go? -> ")
    ConsoleCommands.clear_console()

    if userInputLocation == "1":
      Draw.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Town of Respite\n")
      Draw.welcome()
      Draw.town_of_respite()
      location = locations.TownOfRespite()

    elif userInputLocation == "2":
      Draw.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Fields of Beginning\n")
      Draw.welcome()
      Draw.fields_of_beginning()
      location = locations.FieldsOfBeginning()

    elif userInputLocation == "3":
      Draw.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Middling Marsh\n")
      Draw.welcome()
      Draw.middling_marsh()
      location = locations.MiddlingMarsh()

    elif userInputLocation == "4":
      Draw.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Keep of the End\n")
      Draw.welcome()
      Draw.keep_of_the_end()
      location = locations.KeepOfTheEnd()

    else:
      PrintText.Print_with_delay("That place doesn't exist!\n")

  elif userInputAction == "4" and location.name == "Town of Respite":
    Draw.rest()
    PrintText.Print_with_delay("Your health and magic are restored!\n")
    player.rest()
    if fileLocation is None:
      print("Save files:\n  '1' - file1\n  '2' - file2\n  '3' - file3\n")
      fileNumber = input("Choose save file -> ")
      ConsoleCommands.clear_console()
      fileLocation = f"file{fileNumber}"
    game_state.GameState.save_game(fileLocation, player)

  elif userInputAction == "2":
    PrintText.Print_with_delay("You inspect yourself and your equipment\n")
    Draw.stat_heading()
    player.display_stats()
    Draw.equipment_heading()
    player.display_equipment()

  elif userInputAction == "5":
    PrintText.Print_with_delay("You can switch your current job to any of these:\n")
    jobs = []
    for jobName in player.unlockedJobs:
      jobs.append(jobName)
      print(f"  {len(jobs)} - {jobName}")
    userInputJob = int(input("Which job would you like to change to? -> ")) - 1
    ConsoleCommands.clear_console()
    Draw.job_changed()
    player.switch_job(jobs[userInputJob])

  elif userInputAction == "Q":
    player.health = 0

  else:
    PrintText.Print_with_delay("You can't do that!\n")

Draw.game_over()
