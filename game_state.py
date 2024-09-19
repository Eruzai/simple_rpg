from character import NewPlayerCharacter as Character
from print_delay import PrintText
import pickle

class GameState:
  def __init__(self) -> None:
    pass

  def save_game(fileChoice, playerInfo: Character):
    fileName = f"saved_games/{fileChoice}"
    data = {
      'name': playerInfo.name,
      'unlockedJobs': playerInfo.unlockedJobs,
      'abilities': playerInfo.abilities,
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
      'equipment': playerInfo.equipment,
      'totalEquipmentStats': playerInfo.totalEquipmentStats
    }
    with open(fileName, 'wb') as file:
      pickle.dump(data, file)
      PrintText.Print_with_delay("Game has been saved\n")

  def load_game(fileChoice, playerInfo: Character):
    fileName = f"saved_games/{fileChoice}"
    with open(fileName, 'rb') as file:
      data = pickle.load(file)
      playerInfo.name = data['name']
      playerInfo.unlockedJobs = data['unlockedJobs']
      playerInfo.abilities = data['abilities']
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
      playerInfo.equipment = data['equipment']
      playerInfo.totalEquipmentStats = data['totalEquipmentStats']
      playerInfo.calculate_stats()
      PrintText.Print_with_delay("Game successfully loaded")