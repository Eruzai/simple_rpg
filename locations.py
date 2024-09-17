import enemies, equipment
from print_delay import PrintText
from random import choice

class Location:
  def __init__(self):
     self.encounter = None
     self.treasure = None
  
  def findTreasure(self):
    self.treasure = self.treasures[choice(self.treasureArray)]()
  
  def findNothing(self):
    chance = choice(self.dialogArray)
    dialog = self.dialog[chance]
    PrintText.Print_with_delay(f"{dialog}\n")

  def encounterEnemy(self):
    enemyGroup = []
    for enemyIndex in choice(self.encounterArray):
      enemyGroup.append(self.enemies[enemyIndex]())
    self.encounter = enemyGroup
  
  def explore(self):
    PrintText.Print_with_delay(f"you explore the {self.name}\n")
    chance = choice(self.exploreArray)
    if chance == 1:
      self.findTreasure()
    elif chance == 2:
      self.encounterEnemy()
    elif chance == 3:
      self.findNothing()

class TownOfRespite(Location):
  def __init__(self):
    super().__init__()
    self.name = "Town of Respite"
    self.exploreArray = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
    self.enemies = [enemies.Rat,
                    enemies.RabidDog,
                    enemies.TinySlime,
                    enemies.MysteriousShadow]
    self.encounterArray = [[0, 0], [0, 0, 0, 0, 0], [0, 0, 1], [1, 1], [0, 1], [0, 0, 2], [2, 2], [1, 2], [1, 1, 1], [0, 1, 2], [0, 0, 0, 1], [0, 0, 0], [3]]
    self.treasures = [equipment.StrangeRing,
                      equipment.FragmentOfHope]
    self.treasureArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    self.dialog = ["You nearly miss stepping on a rat. Yikes!",
                   "You walk around and take a breather, It's hard work being an adventurer!",
                   "You hear someone talking about how the fields are full of slimes these days, and some of them are really shiny!",
                   "You feel like you're being watched, and not by rats...",
                   "You hear tales of people dissapearing in town recently, maybe it's the rats?",
                   "Something of a shadow moved in the corner of your vision. It was probably nothing..."]
    self.dialogArray = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]

class FieldsOfBeginning(Location):
  def __init__(self):
    super().__init__()
    self.name = "Fields of Beginning"
    self.exploreArray = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
    self.enemies = [enemies.SmallSlime,
                    enemies.Slime,
                    enemies.Goblin,
                    enemies.SmallSpider,
                    enemies.WindElemental,
                    enemies.ShinySlime]
    self.encounterArray = [[0, 0], [0, 0, 1], [0, 0, 0,], [1, 1], [2, 2, 3, 3], [2, 2], [0, 2], [1, 2], [2, 3], [3, 3, 3], [4], [2, 4], [2, 2, 3], [1, 1, 4], [0, 1, 5]]
    self.treasures = [equipment.RustyHelm,
                      equipment.ClothCap,
                      equipment.RustyMail,
                      equipment.FrayedRobe,
                      equipment.LeatherSandals,
                      equipment.ClothSandals,
                      equipment.AdventuringPants,
                      equipment.WanderingPants,
                      equipment.ShortSword,
                      equipment.GnarledStaff,
                      equipment.GreenRing]
    self.treasureArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.dialog = ["You take a deep breath. The air smells so fresh here.",
                   "It's very easy to walk here, the grass is a bit spongey under your feet.",
                   "It'd be nice if the slimes didn't blend in so well with the grass...",
                   "You sit down for a bit and rest",
                   "Goblins are strong and slimes are tough.",
                   "Don't eat the slimes!",
                   "Sometimes you see something shiny move in the distance."]
    self.dialogArray = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]

class MiddlingMarsh(Location):
  def __init__(self):
    super().__init__()
    self.name = "Middling Marsh"
    self.exploreArray = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
    self.enemies = [enemies.MarshSpider,
                    enemies.Zombie,
                    enemies.GiantRat,
                    enemies.DarkSerpent,
                    enemies.Witch,
                    enemies.WretchedCrow,
                    enemies.MarshHorror]
    self.encounterArray = [[0, 0, 0], [0, 1,], [1, 1], [1, 2, 2], [2, 2], [0, 2], [3, 3], [3, 0], [3, 4], [4, 0, 0], [4, 4], [4, 5, 5], [5, 5, 5], [5, 5, 1], [3, 4], [2, 2, 6]]
    self.treasures = [equipment.HornedHelm,
                      equipment.HeavyHelm,
                      equipment.WitchHat,
                      equipment.MysticCap,
                      equipment.SpikedMail,
                      equipment.SolidChestplate,
                      equipment.WitchRobe,
                      equipment.MysticGarb,
                      equipment.SpurredGreaves,
                      equipment.HeavyBoots,
                      equipment.WitchSlippers,
                      equipment.MysticSandals,
                      equipment.SpurredLeggings,
                      equipment.PlateLeggings,
                      equipment.WitchPants,
                      equipment.MysticSlacks,
                      equipment.BrutalAxe,
                      equipment.Defender,
                      equipment.WitchStaff,
                      equipment.MysticRod,
                      equipment.BlackRing,
                      equipment.WhiteRing]
    self.treasureArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    self.dialog = ["This place is covered in the stench of death.",
                   "A chill wind blows and you hear the sound of chittering and a faint moaning nearby...",
                   "Everything is in shades of grey and brown, It's not a pretty sight.",
                   "You've heard tales of this place, but none compare to actually experiencing it",
                   "Witches are rumoured to have taken up residence here...",
                   "You sometimes feel the ground move beneath your feet. Almost as if it were alive...",
                   "A giant shapeless horror is moving in the distance. Probably best to avoid it..."]
    self.dialogArray = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

class KeepOfTheEnd(Location):
  def __init__(self):
    super().__init__()
    self.name = "Keep of the End"
    self.exploreArray = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
    self.enemies = [enemies.WalkingArmor,
                    enemies.StoneSpider,
                    enemies.AncientSpectre,
                    enemies.ColumnWyrm,
                    enemies.ShadowyCaster,
                    enemies.DancingBlades,
                    enemies.VoidBeast,
                    enemies.TheEnd]
    self.encounterArray = [[0, 0], [0], [0, 5], [5, 5], [1, 1], [1, 1, 1], [2], [2, 2], [2, 6], [3], [3, 3], [4, 6, 6], [4, 4], [4, 2], [6, 6, 6], [6, 6], [7]]
    self.treasures = [equipment.FragmentOfShadow,
                      equipment.NullFragment,
                      equipment.VoidFragment,
                      equipment.ChromaticRing,
                      equipment.UnwieldlyEnd]
    self.treasureArray = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4]
    self.dialog = ["There is no light except for what is provided by the torches on the walls. And even that isn't much to see by...",
                   "The floor is rocky and uneven. This castle must have been built eons ago.",
                   "The air is cold and damp. Just keep moving...",
                   "There are strange sounds coming from all over. It's difficult to pinpoint exactly from where they come...",
                   "You sense an incredible evil here. One that must be eliminated!",
                   "Everything here is dangerous, even the armour!",
                   "The end comes for all of us",
                   "The end is inevitable",
                   "You can not escape your fate..."]
    self.dialogArray = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
