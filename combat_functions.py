import random
from text_functions import inquirer_input
from text_functions import slow_text

# Combat function
def combat(enemies, enemy_object, player_object, items):
    #Ensures that you enter battle with max hp
    player_object.setHealth()
    # For loop to allow for double battles
    for enemy in enemies:
        print("--------------------------------------------------------")
        
        # Add random intros to the battles
        intro = random.randint(1,3)
        match intro:
            case 1:
                slow_text(f"You're fighting against {enemy_object.getName()}")
            case 2:
                slow_text(f"{enemy_object.getName()} attacks")

        # The battle begins   
        while player_object.getHealth() > 0 and enemy_object.getHealth() > 0:
            # Write out player health and enemy health
            print("--------------------------------------------------------")
            slow_text(f"You have {player_object.getHealth()}hp and {enemy_object.getName()} has {enemy_object.getHealth()}hp")
            print("--------------------------------------------------------")
            start_first = random.randint(1,2)
            if start_first == 1:
                slow_text(f"{enemy_object.getName()} is faster than you")
                # Choose a attack for the enemy
                attack_chosen = random.randint(1,2)
                if attack_chosen == 1:
                    enemy_object.attack(player_object)
                    if player_object.getHealth() <= 0:
                        if enemy_object.getName() == "The Revived True Final Boss: Bartolomeus":
                            slow_text("You are defeated")
                            enemies.remove(enemy)
                            return "player died"
                        else:
                            slow_text("You died")
                            exit()
                elif attack_chosen == 2:
                    enemy_object.heal()
                move_choice = inquirer_input(slow_text("What do you want to do?"), ["Attack", "Heal", "Item"])
                if move_choice.lower() == "attack":
                    player_object.attack(enemy_object)
                    if enemy_object.getHealth() <= 0:
                        slow_text("You win the battle")
                        enemies.remove(enemy)
                        break
                elif move_choice.lower() == "heal":
                    player_object.heal()
                elif move_choice.lower() == "item":
                    player_object.use_item(enemy_object)
            elif start_first == 2:
                # Your attack
                move_choice = inquirer_input(slow_text("What do you want to do?"), ["Attack", "Heal", "Item"])
                if move_choice.lower() == "attack":
                    player_object.attack(enemy_object)
                    if enemy_object.getHealth() <= 0:
                        slow_text("You win the battle")
                        enemies.remove(enemy)
                        break
                elif move_choice.lower() == "heal":
                    player_object.heal()
                elif move_choice.lower() == "item":
                    player_object.use_item(enemy_object)
                attack_chosen = random.randint(1,2)
                if attack_chosen == 1:
                    enemy_object.attack(player_object)
                    if player_object.getHealth() <= 0:
                        if enemy_object.getName() == "The Revived True Final Boss: Bartolomeus":
                            slow_text("You are defeated")
                            enemies.remove(enemy)
                            return "player died"
                        else:
                            slow_text("You died")
                            exit()
                elif attack_chosen == 2:
                    enemy_object.heal()
    if enemy_object.getName() == "Shadow Creature":
        max_items(items, player_object)

# Add enemy function
def add_enemy(enemies, enemyName):
    enemies.append(enemyName)

# Make max items 5
def max_items(items, player_object):
    if len(items) == 5:
        slow_text("You can't pick up any more items")
    else:
        player_object.pick_up_item()