from equipment import Item
from character import NewPlayerCharacter as Character
from print_delay import PrintText

class Treasure():
  def __init__(self) -> None:
    pass

  def equip_item(treasure: Item, player: Character):
    slot = treasure.equipSlot
    if player.equipment[slot]:
      equipedItem = player.equipment[slot]
      PrintText.Print_with_delay("Currently equiped item:\n")
      equipedItem.item_stats()
      PrintText.Print_with_delay("Found item:\n")
      treasure.item_stats()
      PrintText.Print_with_delay(f"Would you like to replace your equiped {equipedItem.name} with found {treasure.name}?\n")
      userEquipChoice = input("'y' or 'n' -> ")
      if userEquipChoice == 'y':
        player.equip_item(treasure)
        PrintText.Print_with_delay(f"you equiped the {treasure.name}.\n")
      else:
        PrintText.Print_with_delay(f"you leave the {treasure.name} on the ground and carry on.\n")
    else:
      PrintText.Print_with_delay("Found item:\n")
      treasure.item_stats()
      PrintText.Print_with_delay(f"Would you like to equip {treasure.name}?\n")
      userEquipChoice = input("'y' or 'n' -> ")
      if userEquipChoice == 'y':
        player.equip_item(treasure)
        PrintText.Print_with_delay(f"You equiped the {treasure.name}.\n")
      else:
        PrintText.Print_with_delay(f"You leave the {treasure.name} on the ground and carry on.\n")