import character, locations

print("Welcome to Simple RPG! Please tell us your name before we begin...")

userInputName = input("Enter your character's name -> ")

player = character.NewPlayerCharacter(userInputName)

player.display_stats()

location = locations.TownOfRespite()
fighting = False
treasure = False

while player.health > 0:
  print(f"You are walking around the {location.name}.\nActions:\n  'e' to explore\n  'l' to leave")
  userInputAction = input("What do you do? -> ")
  if userInputAction == "e":
    print("You explore a bit")
    location.explore()
  elif userInputAction == "l":
    print("You open your map and find a few interesting locations nearby...\nLocations:\n  't' - Town of Respite\n  'f' - Fields of Beginning (levels 1 - 5)\n  'm' - Middling Marrow (levels 6 - 10)\n  'k' - Keep of the End (levels 11 - 15)")
    userInputLocation = input("Where would you like to go? -> ")
    if userInputLocation == "t":
      print(f"You leave the {location.name} and travel to the Town of Respite")
      location = locations.TownOfRespite()
    elif userInputLocation == "f":
      print(f"You leave the {location.name} and travel to the Fields of Beginning")
      location = locations.FieldsOfBeginning()
    elif userInputLocation == "m":
      print(f"You leave the {location.name} and travel to the Middling Marrow")
      location = locations.MiddlingMarrow()
    elif userInputLocation == "f":
      print(f"You leave the {location.name} and travel to the Keep of the End")
      location = locations.KeepOfTheEnd()
    else:
      print("That place doesn't exist!")
  else:
    print("You can't do that!")

print("your quest is over")
