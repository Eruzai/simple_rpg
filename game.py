import game_state, character, locations, encounter, found_treasure, ascii_art
from console import ConsoleCommands
from print_delay import PrintText

art = ascii_art.Draw()

art.welcome()
art.title()

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

art.stat_heading()
player.display_stats()

art.welcome()
art.town_of_respite()
location = locations.TownOfRespite()

while player.health > 0:
  PrintText.Print_with_delay(f"You are walking around the {location.name}.\n")
  print("Actions:\n  'e' - explore\n  'i' - inspect stats and equipment\n  'l' - leave\n")

  if len(player.unlockedJobs) > 1:
    print("  'c' - change current job")

  if location.name == "Town of Respite":
    print("  'r' - rest at the inn and save game\n  'q' - quit game\n")

  userInputAction = input("What do you want to do? -> ")
  ConsoleCommands.clear_console()

  if userInputAction == "e":
    art.exploring()
    location.explore()

    if location.encounter:
      art.battle_notification()
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

  elif userInputAction == "l":
    art.open_map()
    PrintText.Print_with_delay("There are a few interesting locations nearby...\n")
    print("Locations:\n  't' - Town of Respite\n  'f' - Fields of Beginning (levels 1 - 5)\n  'm' - Middling Marrow (levels 6 - 10)\n  'k' - Keep of the End (levels 11 - 15)\n")
    userInputLocation = input("Where would you like to go? -> ")
    ConsoleCommands.clear_console()

    if userInputLocation == "t":
      art.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Town of Respite\n")
      art.welcome()
      art.town_of_respite()
      location = locations.TownOfRespite()

    elif userInputLocation == "f":
      art.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Fields of Beginning\n")
      art.welcome()
      art.fields_of_beginning()
      location = locations.FieldsOfBeginning()

    elif userInputLocation == "m":
      art.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Middling Marsh\n")
      art.welcome()
      art.middling_marsh()
      location = locations.MiddlingMarsh()

    elif userInputLocation == "k":
      art.travelling()
      PrintText.Print_with_delay(f"You leave the {location.name} and head towards the Keep of the End\n")
      art.welcome()
      art.keep_of_the_end()
      location = locations.KeepOfTheEnd()

    else:
      PrintText.Print_with_delay("That place doesn't exist!\n")

  elif userInputAction == "r" and location.name == "Town of Respite":
    art.rest()
    PrintText.Print_with_delay("Your health and magic are restored!\n")
    player.rest()
    if fileLocation is None:
      print("Save files:\n  '1' - file1\n  '2' - file2\n  '3' - file3\n")
      fileNumber = input("Choose save file -> ")
      ConsoleCommands.clear_console()
      fileLocation = f"file{fileNumber}"
    game_state.GameState.save_game(fileLocation, player)

  elif userInputAction == "i":
    PrintText.Print_with_delay("You inspect yourself and your equipment\n")
    art.stat_heading()
    player.display_stats()
    art.equipment_heading()
    player.display_equipment()

  elif userInputAction == "c":
    PrintText.Print_with_delay("You can switch your current job to any of these:\n")
    for jobName in player.unlockedJobs:
      print(f"  {jobName}")
    userInputJob = input("Which job would you like to change to? (type full name) -> ")
    ConsoleCommands.clear_console()
    art.job_changed()
    player.switch_job(userInputJob)

  elif userInputAction == "q":
    player.health = 0

  else:
    PrintText.Print_with_delay("You can't do that!\n")

art.game_over()
