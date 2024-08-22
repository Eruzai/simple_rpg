class newCharacter:
  def __init__(self, characterJob, healthPoints, magicPoints, strength, intelect):
    self.job = characterJob
    self.hp = healthPoints
    self.mp = magicPoints
    self.str = strength
    self.int = intelect

userInputJob = input("You start playing as a warrior!\nWould you like to play as a wizard instead?\nEnter Y for wizard or just hit enter to continue as a warrior -> ")

job = "warrior"

if userInputJob is "Y":
  job = "wizard"

player = newCharacter(job, 10, 20, 30, 40)

print("I am a {job}! I have {str} strength".format(job=player.job, str=player.str))