import character

print("Welcome to Simple RPG! Please tell us your name before we begin...")

userInputName = input("Enter your character's name: ")

player1 = character.NewPlayerCharacter(userInputName)

player1.display_stats()

player1.class_change()

player1.display_stats()
