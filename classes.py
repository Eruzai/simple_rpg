from random import randint

class newCharacter:
  def __init__(self, characterJob, healthPoints, magicPoints, strength, intellect):
    self.job = characterJob
    self.hp = healthPoints
    self.mp = magicPoints
    self.str = strength
    self.int = intellect

userInputJob = input("You start playing as a warrior!\nWould you like to play as a wizard instead?\nEnter Y for wizard or just hit enter to continue as a warrior -> ")

job = "warrior"
strength = randint(35, 50)
intellect = randint(5, 15)
healthpoints = 50 + strength // 1.5
magicpoints = 5 + intellect // 3

if userInputJob == "Y":
  job = "wizard"
  strength = randint(5, 15)
  intellect = randint(35, 50)
  healthpoints = 30 + strength // 3
  magicpoints = 50 + intellect // 1.5

player = newCharacter(job, healthpoints, magicpoints, strength, intellect)

print("I am a {job}!\nI have {hp} health points.\nI have {mp} magic points.\nI have {str} strength.\nI have {int} intellect.".format(job=player.job, hp=player.hp, mp=player.mp, str=player.str, int=player.int))