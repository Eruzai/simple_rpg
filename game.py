import character, locations

print("Welcome to Simple RPG! Please tell us your name before we begin...")

userInputName = input("Enter your character's name -> ")

player = character.NewPlayerCharacter(userInputName)

player.display_stats()

location = locations.TownOfRespite()

while player.health > 0:
  print(f"You are walking around the {location.name}.\nActions:\n  'e' to explore\n  'l' to leave")
  if location.name == "Town of Respite":
    print("  'r' - to rest at an inn")
  userInputAction = input("What do you do? -> ")
  if userInputAction == "e":
    print("You explore a bit")
    location.explore()
    while location.enemy and location.enemy.health > 0 and player.health > 0:
      print("Actions:\n  'a' - attack\n  'm' - magical attack\n  'i' - inspect enemy\n  'r' - run away")
      userInputAction = input("What do you do? -> ")
      if userInputAction == "a":
        damage = player.strength
        if hasattr(location.enemy, 'physicalDef'):
          enemyDefMultiplier = location.enemy.physicalDef / 100
          damage = player.strength - player.strength * enemyDefMultiplier // 1
        location.enemy.damage_taken(damage)
        print(f"You inflict {damage} points of physical damage to {location.enemy.name}")
      elif userInputAction == "m":
        damage = player.intellect
        if hasattr(location.enemy, 'magicDef'):
          enemyDefMultiplier = location.enemy.magicDef / 100
          damage = player.intellect - player.intellect * enemyDefMultiplier // 1
        location.enemy.damage_taken(damage)
        print(f"You inflict {damage} points of magical damage to {location.enemy.name}")
      elif userInputAction == "i":
        location.enemy.display_stats()
      elif userInputAction == "r":
        print(f"You run away from {location.enemy.name}")
        location.enemy = None
      else:
        print("That's not a valid action")
    
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
  elif userInputAction == "r":
    print("You rest at the inn.\nYour health and magic are restored!")
    player.rest()
  else:
    print("You can't do that!")

print("your quest is over")
