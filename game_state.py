from character import NewPlayerCharacter as Character
import pickle

class GameState:
  def __init__(self) -> None:
    pass

  def save_game(fileChoice, playerInfo: Character):
    fileName = f"saved_games/{fileChoice}"
    data = {
      'name': playerInfo.name,
      'unlockedJobs': playerInfo.unlockedJobs,
      'job': playerInfo.job,
      'level': playerInfo.level,
      'experience': playerInfo.experience,
      'experienceNeeded': playerInfo.experienceNeeded,
      'baseMaxHealth': playerInfo.baseMaxHealth,
      'health': playerInfo.health,
      'baseMaxMagic': playerInfo.baseMaxMagic,
      'magic': playerInfo.magic,
      'baseStrength': playerInfo.baseStrength,
      'baseIntellect': playerInfo.baseIntellect,
      'basePhysicalDef': playerInfo.basePhysicalDef,
      'baseMagicDef': playerInfo.baseMagicDef,
      'head': playerInfo.head,
      'body': playerInfo.body,
      'weapon': playerInfo.weapon,
      'legs': playerInfo.legs,
      'feet': playerInfo.feet,
      'ring': playerInfo.ring
    }
    with open(fileName, 'wb') as file:
      pickle.dump(data, file)

  def load_game(fileChoice, playerInfo: Character):
    fileName = f"saved_games/{fileChoice}"
    with open(fileName, 'rb') as file:
      data = pickle.load(file)
      playerInfo.name = data['name']
      playerInfo.unlockedJobs = data['unlockedJobs']
      playerInfo.job = data['job']
      playerInfo.level = data['level']
      playerInfo.experience = data['experience']
      playerInfo.experienceNeeded = data['experienceNeeded']
      playerInfo.baseMaxHealth = data['baseMaxHealth']
      playerInfo.health = data['health']
      playerInfo.baseMaxMagic = data['baseMaxMagic']
      playerInfo.magic = data['magic']
      playerInfo.baseStrength = data['baseStrength']
      playerInfo.baseIntellect = data['baseIntellect']
      playerInfo.basePhysicalDef = data['basePhysicalDef']
      playerInfo.baseMagicDef = data['baseMagicDef']
      playerInfo.head = data['head']
      playerInfo.body = data['body']
      playerInfo.weapon = data['weapon']
      playerInfo.legs = data['legs']
      playerInfo.feet = data['feet']
      playerInfo.ring = data['ring']
      playerInfo.calculate_stats()
      playerInfo.display_stats()