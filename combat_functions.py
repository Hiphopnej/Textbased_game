import random
from text_functions import inquirer_input
from text_functions import slow_text

# Combat function
def combat(enemies, enemy_object, player_object, items, amount):
    enemies = add_enemy(enemies, enemy_object.getName(), amount)
    #Ensures that you enter battle with max hp
    player_object.setHealth(200)
    enemy_health = enemy_object.getHealth()
    # While loop to allow for battles against multiple enemies
    while True:
        if len(enemies) > 0:
            enemy = enemies[0]
            print("--------------------------------------------------------")
            if enemy == "The True Final Boss: Bartolomeus" or enemy == "The Revived True Final Boss: Bartolomeus":
                slow_text(f"{enemy_object.getName()} attacks", 0.1)
            else:
                # Add random intros to the battles
                intro = random.randint(1,2)
                match intro:
                    case 1:
                        slow_text(f"You're fighting against {enemy_object.getName()}", 0.04)
                    case 2:
                        slow_text(f"{enemy_object.getName()} attacks", 0.04)

            # The battle begins   
            while player_object.getHealth() > 0 and enemy_object.getHealth() > 0:
                # Write out player health and enemy health
                print("--------------------------------------------------------")
                slow_text(f"You have {player_object.getHealth()}hp and {enemy_object.getName()} has {enemy_object.getHealth()}hp", 0.04)
                print("--------------------------------------------------------")
                start_first = random.randint(1,2)
                if start_first == 1:
                    slow_text(f"{enemy_object.getName()} is faster than you", 0.04)
                    # Choose a attack for the enemy
                    attack_chosen = random.randint(1,2)
                    if attack_chosen == 1:
                        enemy_object.attack(player_object)
                        if player_object.getHealth() <= 0:
                            if enemy_object.getName() == "The Revived True Final Boss: Bartolomeus":
                                slow_text("You are defeated", 0.04)
                                return "player died to final boss"
                            else:
                                slow_text("You died", 0.04)
                                return "you died"
                    elif attack_chosen == 2:
                        enemy_object.heal()
                    move_choice = inquirer_input(slow_text("What do you want to do?", 0.04), ["Attack", "Heal", "Item"])
                    if move_choice.lower() == "attack":
                        player_object.attack(enemy_object)
                        if enemy_object.getHealth() <= 0:
                            slow_text("You win the battle", 0.04)
                            enemy_object.setHealth(enemy_health)
                            enemies.remove(enemy_object.getName())
                            if len(enemies) <= 1:
                                if enemy_object.getName() == "Shadow Creature":
                                    max_items(items, player_object)
                                return "You won"
                            elif len(enemies) > 1:
                                continue
                    elif move_choice.lower() == "heal":
                        player_object.heal()
                    elif move_choice.lower() == "item":
                        player_object.use_item(enemy_object)
                elif start_first == 2:
                    # Your attack
                    move_choice = inquirer_input(slow_text("What do you want to do?", 0.04), ["Attack", "Heal", "Item"])
                    if move_choice.lower() == "attack":
                        player_object.attack(enemy_object)
                        if enemy_object.getHealth() <= 0:
                            slow_text("You win the battle", 0.04)
                            enemy_object.setHealth(enemy_health)
                            enemies.remove(enemy_object.getName())
                            if len(enemies) <= 0:
                                if enemy_object.getName() == "Shadow Creature":
                                    max_items(items, player_object)
                                return "You won"
                            elif len(enemies) > 0:
                                continue
                    elif move_choice.lower() == "heal":
                        player_object.heal()
                    elif move_choice.lower() == "item":
                        player_object.use_item(enemy_object)
                    attack_chosen = random.randint(1,2)
                    if attack_chosen == 1:
                        enemy_object.attack(player_object)
                        if player_object.getHealth() <= 0:
                            if enemy_object.getName() == "The Revived True Final Boss: Bartolomeus":
                                slow_text("You are defeated", 0.04)
                                return "player died to final boss"
                            else:
                                slow_text("You died", 0.04)
                                return "you died"
                    elif attack_chosen == 2:
                        enemy_object.heal()

# Add enemy function
def add_enemy(enemies, enemyName, amount):
    while amount > 0:
        enemies.append(enemyName)
        amount -= 1
    return enemies

# Make max items 5
def max_items(items, player_object):
    if len(items) == 5:
        slow_text("You can't pick up any more items", 0.04)
    else:
        player_object.pick_up_item()