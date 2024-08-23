import character, locations

print("Welcome to Simple RPG! Please tell us your name before we begin...")

userInputName = input("Enter your character's name: ")

player = character.NewPlayerCharacter(userInputName)

player.display_stats()

location = locations.TownOfRespite

while player.health > 0:
  while location == locations.TownOfRespite:
    print(f"You are walking around the {location.name}. What would you like to do?")
    userInputAction = input("Actions: explore, go to fields\nType your action: ")
    if userInputAction == "explore":
      print("You explore a bit")
      location.explore(location)
    elif userInputAction == "go to fields":
      print("You leave town and travel towards the Fields of Beginning")
      location = locations.FieldsOfBeginning
    else:
      print("You can't do that!")
  
  while location == locations.FieldsOfBeginning:
    print(f"You are standing in the {location.name}, what would you like to do?")
    userInputAction = input("Actions: explore, go to town\nType your action: ")
    if userInputAction == "explore":
      print("You walk around the fields a bit")
      location.explore(location)
    elif userInputAction == "go to town":
      print("you head into town")
      location = locations.TownOfRespite
    else:
      print("You can't do that!")

print("your quest is over")
