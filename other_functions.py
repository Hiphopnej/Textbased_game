from text_functions import slow_text
from combat_functions import combat
from combat_functions import add_enemy
from combat_functions import max_items

# Credits
def game_credits():
    slow_text("Code by Alvar Eklind")
    slow_text("Story by Alvar Eklind")
    slow_text("Thanks for playing and hope you enjoyed yourself")

# The final boss of the door ending
# Called with final_door_fight(player, forest_shadow, enemies)
def final_door_fight(player_object, enemy_object, enemies, items):
    slow_text(f"When {player_object.getName()} went though the next door he finally got to the final room")
    slow_text("There he meets")
    slow_text("The final boss: The forest shadow")
    slow_text("This is gonna be hard")

    if "Godslayer" in items:
        items.remove("Godslayer")

    add_enemy(enemies, enemy_object.getName())
    combat(enemies, enemy_object, player_object)
    slow_text(f"When {player_object.getName()} defeated the forest shadow the temple suddenly started to fall together")
    slow_text(f"{player_object.getName()} tries to escapes but sadly doesn't have enough time")
    slow_text(f"The evil mystery is now solved and legends of {player_object.getName()} was told for decades to come")
    slow_text("The end")
    game_credits()

# Code for door ending
def door_code(which_door, amount_of_enemies, enemy_object, player_object, enemies, items):
    slow_text(f"You take the {which_door} door")
    slow_text(f"There is {amount_of_enemies} in the room")
    if amount_of_enemies == 1:
        add_enemy(enemies, enemy_object.getName())
        combat(enemies, enemy_object, player_object)
        max_items(items, player_object)
    elif amount_of_enemies == 2:
        add_enemy(enemies, enemy_object.getName())
        add_enemy(enemies, enemy_object.getName())
        combat(enemies, enemy_object, player_object)
        max_items(items, player_object)
        max_items(items, player_object)
    elif amount_of_enemies == 3:
        add_enemy(enemies, enemy_object.getName())
        add_enemy(enemies, enemy_object.getName())
        add_enemy(enemies, enemy_object.getName())
        combat(enemies, enemy_object, player_object)
        max_items(items, player_object)
        max_items(items, player_object)
        max_items(items, player_object)