from random import randint, choice
import copy
from character import NewPlayerCharacter as player
from enemies import Enemy

class Summon:
  def execute(encounter, enemyToSummon):
    encounter.append(enemyToSummon)

class Divide:
  def execute(encounter, enemy: Enemy):
    enemy.health = enemy.health // 2
    newEnemy = copy.deepcopy(enemy)
    encounter.append(newEnemy)

class Consume:
  def execute(encounter, attackingEnemy: Enemy):
    choices = []
    for index, enemy in enumerate(encounter):
      if enemy is not attackingEnemy:
        choices.append(index)
    targetIndex = choice(choices)
    target = encounter[targetIndex]
    attackingEnemy.health += target.health
    del encounter[targetIndex]

class Bite:
  def execute(player: player, enemy: Enemy):
    damage = enemy.strength * 1.2
    player.damage_taken(damage, "physical")