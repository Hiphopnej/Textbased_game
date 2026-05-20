from text_functions import slow_text, inquirer_input
from combat_functions import combat, add_enemy, max_items
from save_functions import save_game
from classes import Player

# Credits
def game_credits():
    slow_text("Code by Alvar Eklind", 0.04)
    slow_text("Story by Alvar Eklind", 0.04)
    slow_text("Thanks for playing and hope you enjoyed yourself", 0.04)

def check_godslayer(enemies, player_object):
    if len(player_object.godslayer_list) > 0:
        player_object.inventory.remove("Godslayer")
        slow_text("You feel the Godslayer shaking", 0.04)
        slow_text("The enemies you used Godslayer on return stronger????", 0.04)

        # Go though godslayer list and fight every enemy you used godslayer on back to back
        for enemy_name in player_object.godslayer_list:
            # Add the enemy to enemies list
            enemies.append(enemy_name)
# The final boss of the door ending
# Called with final_door_fight(player, forest_shadow, enemies)
def final_door_fight(player_object, enemy_object, enemies):
    enemies.clear()
    slow_text(f"When {player_object.getName()} went though the next door he finally got to the final room", 0.04)
    slow_text("There he meets", 0.04)
    slow_text("The final boss: The forest shadow", 0.1)
    slow_text("This is gonna be hard", 0.04)

    check_godslayer(enemies, player_object)

    # Add the final boss
    enemies.append(enemy_object.getName())
    combat(enemies, enemy_object, player_object, player_object.inventory)
    slow_text(f"When {player_object.getName()} defeated the forest shadow the temple suddenly started to fall together", 0.04)
    slow_text(f"{player_object.getName()} tries to escapes but sadly doesn't have enough time", 0.04)
    slow_text(f"The evil mystery is now solved and legends of {player_object.getName()} was told for decades to come", 0.04)
    slow_text("The end", 0.1)
    player_object.godslayer_list.clear()
    game_credits()

# Code for door ending
def door_code(which_door, amount_of_enemies, enemy_object, player_object, enemies):
    slow_text(f"You take the {which_door} door", 0.04)
    slow_text(f"There is {amount_of_enemies} in the room", 0.04)
    if amount_of_enemies == 1:
        add_enemy(enemies, enemy_object.getName(), 1)
        combat(enemies, enemy_object, player_object, player_object.inventory)
    elif amount_of_enemies == 2:
        add_enemy(enemies, enemy_object.getName(), 2)
        combat(enemies, enemy_object, player_object, player_object.inventory)
    elif amount_of_enemies == 3:
        add_enemy(enemies, enemy_object.getName(), 3)
        combat(enemies, enemy_object, player_object, player_object.inventory)

def create_charachter():
    player_name = input("Enter your name ")  
    player_class = inquirer_input(slow_text("Choose a class", 0.04), ["Mage", "Warrior"])
    player = Player(player_name, player_class)
    #Create a json file with the same name as the player name
    save_game(player, 0)
    return player