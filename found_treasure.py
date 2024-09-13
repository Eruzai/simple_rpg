from equipment import Item
from character import NewPlayerCharacter as Character

class Treasure():
  def __init__(self) -> None:
    pass

  def equip_item(treasure: Item, player: Character):
    slot = treasure.equipSlot
    if player.equipment[slot]:
      equipedItem = player.equipment[slot]
      print("Currently equiped item:")
      equipedItem.item_stats()
      print("Found item:")
      treasure.item_stats()
      print(f"Would you like to replace your equiped {equipedItem.name} with found {treasure.name}?")
      userEquipChoice = input("'y' or 'n' -> ")
      if userEquipChoice == 'y':
        player.equip_item(treasure)
        print(f"you equiped the {treasure.name}.")
      else:
        print(f"you leave the {treasure.name} on the ground and carry on.")
    else:
      player.equip_item(treasure)
      print(f"you equiped the {treasure.name}.")