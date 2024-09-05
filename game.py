import game_state, character, locations, encounter, ascii_art

art = ascii_art.Draw()

art.welcome()
art.title()

print("Actions:\n  'n' - start new game\n  'l' - load game")
userInputLoadGame = input("-> ")

if userInputLoadGame == 'l':
  print("Save files:\n  '1' - file1\n  '2' - file2\n  '3' - file3")
  fileNumber = input("Choose save file -> ")
  fileLocation = f"file{fileNumber}"
  player = character.NewPlayerCharacter('noname')
  game_state.GameState.load_game(fileLocation, player)
elif userInputLoadGame == 'n':
  userInputName = input("Enter your character's name -> ")
  player = character.NewPlayerCharacter(userInputName)
  fileLocation = None

art.stat_heading()
player.display_stats()

art.welcome()
art.town_of_respite()
location = locations.TownOfRespite()

while player.health > 0:
  print(f"You are walking around the {location.name}.\n\nActions:\n  'e' - explore\n  'i' - inspect stats and equipment\n  'l' - leave")

  if len(player.unlockedJobs) > 1:
    print("  'c' - change current job")

  if location.name == "Town of Respite":
    print("  'r' - rest at the inn and save game\n  'q' - quit game")

  userInputAction = input("What do you want to do? -> ")

  if userInputAction == "e":
    art.exploring()
    location.explore()

    if location.enemy:
      art.battle_notification()
      print(f"A level {location.enemy.level} {location.enemy.name} appears before you!")
      location.enemy.draw()
      encounter.Fight.battle(location.enemy, player)
      location.enemy = None

  elif userInputAction == "l":
    art.open_map()
    print("There are a few interesting locations nearby...\n\nLocations:\n  't' - Town of Respite\n  'f' - Fields of Beginning (levels 1 - 5)\n  'm' - Middling Marrow (levels 6 - 10)\n  'k' - Keep of the End (levels 11 - 15)")
    userInputLocation = input("Where would you like to go? -> ")

    if userInputLocation == "t":
      print(f"You leave the {location.name} and head towards the Town of Respite")
      art.travelling()
      art.welcome()
      art.town_of_respite()
      location = locations.TownOfRespite()

    elif userInputLocation == "f":
      print(f"You leave the {location.name} and head towards the Fields of Beginning")
      art.travelling()
      art.welcome()
      art.fields_of_beginning()
      location = locations.FieldsOfBeginning()

    elif userInputLocation == "m":
      print(f"You leave the {location.name} and head towards the Middling Marsh")
      art.travelling()
      art.welcome()
      art.middling_marsh()
      location = locations.MiddlingMarsh()

    elif userInputLocation == "k":
      print(f"You leave the {location.name} and head towards the Keep of the End")
      art.travelling()
      art.welcome()
      art.keep_of_the_end()
      location = locations.KeepOfTheEnd()

    else:
      print("That place doesn't exist!")

  elif userInputAction == "r" and location.name == "Town of Respite":
    art.rest()
    print("Your health and magic are restored!\n")
    player.rest()
    if fileLocation is None:
      print("Save files:\n  '1' - file1\n  '2' - file2\n  '3' - file3")
      fileNumber = input("Choose save file -> ")
      fileLocation = f"file{fileNumber}"
    game_state.GameState.save_game(fileLocation, player)

  elif userInputAction == "i":
    print("You inspect yourself and your equipment")
    art.stat_heading()
    player.display_stats()
    art.equipment_heading()
    player.display_equipment()

  elif userInputAction == "c":
    print("You can switch your current job to any of these:")
    for jobName in player.unlockedJobs:
      print(f"  {jobName}")
    userInputJob = input("Which job would you like to change to? (type full name) -> ")
    art.job_changed()
    player.switch_job(userInputJob)

  elif userInputAction == "q":
    player.health = 0

  else:
    print("You can't do that!")

art.game_over()
