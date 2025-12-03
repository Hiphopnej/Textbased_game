import random
from InquirerPy import inquirer
import time

"""
How to write inquirer
choice = inquirer.select(
    message="welcome",
    choices = ["Start", "End"]
).execute()
"""
def inquirer_input(message_param, options):
    choice = inquirer.select(
        message=message_param,
        choices = options
    ).execute()
    return choice

def slow_text(message):
    message += "\n"
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(0.03)

class Charachter:
    # Initiate all varibles
    def __init__(self, health, dmgLower, dmgHigher, base_dmg, healingLower, healingHigher, name):
        self.health = health
        self.dmgLower = dmgLower
        self.dmgHigher = dmgHigher
        self.base_dmg = base_dmg
        self.healingLower = healingLower
        self.healingHigher = healingHigher
        self.name = name

    def take_damage(self, damage_taken):
        self.health -= damage_taken
    
    def attack(self, enemy_object):
        # Calulate dmg
        dmg = random.randint(self.dmgLower, self.dmgHigher)

        # Calculate crit
        crit = random.randint(1,20)

        # Calculate total damage
        total_dmg = self.base_dmg + dmg

        # Deals dmg based on if critted or not
        if crit == 11:
            crit_dmg = total_dmg * 1.5
            enemy_object.take_damage(crit_dmg)
            slow_text(f"You got a crit and dealt {crit_dmg} to {enemy_object.name}")
        else:
            enemy_object.take_damage(total_dmg)
            slow_text(f"{enemy_object.name} took {total_dmg} amount of dmg")
    
    def heal(self):
        # Calculate heal amount
        heal_amount = random.randint(self.healingLower, self.healingHigher)

        # Heal
        self.health += heal_amount
        slow_text(f"{self.name} healed {heal_amount}hp and now their total hp is: {self.health}hp")

    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health

# Player class that inherits from Charachter class
class Player(Charachter):
    def __init__(self, health, dmgLower, dmgHigher, base_dmg, healingLower, healingHigher, name, inventory):
        self.health = health
        self.dmgLower = dmgLower
        self.dmgHigher = dmgHigher
        self.base_dmg = base_dmg
        self.healingLower = healingLower
        self.healingHigher = healingHigher
        self.name = name
        self.inventory = inventory

    def pick_up_item(self):
        item_number = random.randint(1,1000)
        if item_number == 1000:
            self.inventory.append("ecologic egg launcher")
            slow_text("You got a Ecologic egg launcher")
        elif item_number >= 989 and item_number < 1000:
            self.inventory.append("godslayer")
            slow_text("You got the Godslayer")
        elif item_number >= 0 and item_number <= 495:
            self.inventory.append("attack brew")
            slow_text("You got a attack brew")
        else:
            self.inventory.append("health brew")
            slow_text("You got a health brew")

    def use_item(self, enemy_object):
        if len(self.inventory) <= 0:
            slow_text("You don't have any items")
        else:
            chosen_item = inquirer_input(f"What item do you want to use: {self.inventory}", [self.inventory])
            if chosen_item == "ecologic egg launcher":
                enemy_object.take_damage(1)
                slow_text(f"{enemy_object.name} took 1 dmg")
            elif chosen_item == "godslayer":
                enemy_object.take_damage(1000000000000)
                slow_text(f"{enemy_object.name} took 1000000000000 dmg")
            elif chosen_item == "attack potion":
                enemy_object.take_damage(80)
                slow_text(f"{enemy_object.name} took 80 dmg")
                self.inventory.remove("attack potion")
            elif chosen_item == "health potion":
                self.health += 100
                self.inventory.remove("health potion")

# Credits
def credits():
    slow_text("Code by Alvar Eklind")
    slow_text("Story by Alvar Eklind")
    slow_text("Thanks for playing and hope you enjoyed yourself")

# Combat function
def combat(enemies, enemy_object, player_object):
    # For loop to allow for double battles
    for enemy in enemies:
        print("--------------------------------------------------------")
        
        # Add random intros to the battles
        intro = random.randint(1,3)
        match intro:
            case 1:
                slow_text(f"A {enemy_object.getName()} has appeared")
            case 2:
                slow_text(f"You're fighting against a {enemy_object.getName()}")
            case 3:
                slow_text(f"A {enemy_object.getName()} attacks")

        # The battle begins   
        while player_object.getHealth() > 0 and enemy_object.getHealth() > 0:
            # Write out player health and enemy health
            print("--------------------------------------------------------")
            slow_text(f"You have {player_object.getHealth()}hp and {enemy_object.getName()} has {enemy_object.getHealth()}hp")
            print("--------------------------------------------------------")
            start_first = random.randint(1,2)
            if start_first == 1:
                slow_text(f"{player_object.getHealth()} is faster than you")
                # Choose a attack for the enemy
                attack_chosen = random.randint(1,2)
                if attack_chosen == 1:
                    enemy_object.attack(player_object)
                    if player_object.getHealth() <= 0:
                        slow_text("You died")
                        exit()
                elif attack_chosen == 2:
                    enemy_object.heal()
                move_choice = inquirer_input(slow_text("What do you want to do?"), ["Attack", "Heal", "Item"])
                if move_choice.lower() == "attack":
                    player_object.attack(enemy_object)
                    if enemy_object.getHealth() <= 0:
                        slow_text("You win the battle")
                        enemies.remove(enemy_object.getName())
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
                        enemies.remove(enemy_object.getName())
                        break
                elif move_choice.lower() == "heal":
                    player_object.heal()
                elif move_choice.lower() == "item":
                    player_object.use_item(enemy_object)
                attack_chosen = random.randint(1,2)
                if attack_chosen == 1:
                    enemy_object.attack(player_object)
                    if player_object.getHealth() <= 0:
                        slow_text("You died")
                        exit()
                elif attack_chosen == 2:
                    enemy_object.heal()

# Add enemy function
"""
    Add enemy shall be used as many times as the amount of enemy you are suppuoesed to fight
    Example with two enemys:
    add_enemy(enemys, "Shadow creature");
    add_enemy(enemys, "Shadow creature");
    combat(enemys)
    where enemy is a list
"""

def add_enemy(enemies, enemyName):
    enemies.append(enemyName)

# Make max items 5
def max_items(items, player_object):
    if len(items) == 5:
        slow_text("You can't pick up any more items")
    else:
        player_object.pick_up_item()

# The final boss of the door ending
# Called with final_door_fight(player, forest_shadow, enemies)
def final_door_fight(player_object, enemy_object, enemies):
    slow_text(f"When {player_object.getName()} went though the next door he finally got to the final room")
    slow_text("There he meets")
    slow_text("The final boss: The forest shadow")
    slow_text("This is gonna be hard")
    add_enemy(enemies, enemy_object.getName())
    combat(enemies, enemy_object, player_object)
    slow_text(f"When {player_object.getName()} defeated the forest shadow the temple suddenly started to fall together")
    slow_text(f"{player_object.getName()} tries to escapes but sadly doesn't have enough time")
    slow_text(f"The evil mystery is now solved and legends of {player_object.getName()} was told for decades to come")
    slow_text("The end")
    credits()

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

# main

# lists
enemies = []
items = []

player_name = input("Enter your name ")

# Create all objects
player = Player(200, 20, 90, 10, 50, 80, player_name, items)
forest_beast = Charachter(50, 10, 20, 5, 10, 20, "Forest Beast")
shadow_creature = Charachter(100, 30, 50, 10, 20, 30, "Shadow Creature")
the_forest_shadow = Charachter(150, 50, 70, 10, 30, 40, "The Final Boss: The Forest Shadow")
# Hard mode objects
forest_beast_hard = Charachter(75, 15, 30, 10, 15, 30, "Forest Beast")
shadow_creature_hard = Charachter(150, 45, 75, 15, 35, 50, "Shadow Creature")
the_forest_shadow_hard = Charachter(200, 50, 80, 10 ,45, 60, "The Final Boss: The Forest Shadow")
# Hardest boss in the game
Bartolomeus = Charachter(250, 50, 90, 15 ,45, 60, "The True Final Boss: Bartolomeus")

# Asks if you want to know the rules
rule_choice = inquirer_input(slow_text("Do you want to know the rules?"), ["Yes", "No"])

if rule_choice == "Yes":
    print("--------------------------------------------------------")
    slow_text("Welcome to The Forest Adventure")
    slow_text("This is a turnbased game the allows you to choose your own path")
    slow_text("After each fight you will get full health except for if you encounter multiple enemies")
    slow_text("You get an item each time you kill a shadow creature but you can only have a maximum of five items")
    slow_text("There are a total of four different items you can find with varying rarities and effects")
    slow_text("You max damage and healing is 100 and 80 respectivly")
    slow_text("You and the enemy have a 5 percent chance to crit which deals 1.5x damage")
    slow_text("Good luck and have fun")
    print("--------------------------------------------------------")

are_you_ready = inquirer_input(slow_text("Are you ready to start?"), ["Yes"])

# The game begins
slow_text("There once ws a mysterious forest")
slow_text("It was dim and quiet and all who lived in the nearby village was telling scary stories about it")
slow_text(f"One day {player.getName()} decided to try to investigate the mystery surrounding the forest so that no one has to be afraid anymore")
slow_text(f"{player.getName()} takes his sword and enters the forest")
slow_text("I wonder what can be so mysterious about this forest")
camp_choice = inquirer_input(slow_text("Should I first put up a camp or should I continue exploring?"), ["Camp", "Explore"])

# Camp route
if camp_choice == "Camp":
    slow_text("I should probably put up a camp first")
    slow_text("What is this?")
    player.pick_up_item()
    slow_text(f"{player.getName()} was getting ready to sleep when suddenly")
    slow_text("A forest beast appears")
    # Your very first fight
    add_enemy(enemies, forest_beast.getName())
    combat(enemies, forest_beast, player)
    slow_text("That was close, hope it's safe to sleep now")
    print("--------------------------------------------------------")
    slow_text("The next day")
    print("--------------------------------------------------------")
    slow_text("I need to find out where the monster came from")
    slow_text("I should try to get to the middle of the forest")
    slow_text(f"When {player.getName()} gets farther in he finds a shadow creature")
    add_enemy(enemies, shadow_creature.getName())
    combat(enemies, shadow_creature, player)
    max_items(items, player)
    slow_text("That shadow creature was stronger than that forest beast")
    slow_text("It must be related to the mystery")
    slow_text(f"When {player.getName()} get to the middle of the forest, he discovers a temple")
    slow_text(f"This temple must be related to the evil of this forest")
    temple_path_choice = inquirer_input(slow_text("Should I try to find a path around or just go in at the front?"), ["Front", "Back"])

    # Front route
    if temple_path_choice == "Front":
        slow_text(f"When {player.getName()} enters the temple he encounters two shadow creatures")
        add_enemy(enemies, shadow_creature.getName())
        add_enemy(enemies, shadow_creature.getName())
        combat(enemies, shadow_creature, player)
        max_items(items, player)
        
        #The door path begins
        slow_text(f"When {player.getName()} enters the temple he encounters two shadow creatures")
        add_enemy(enemies, shadow_creature.getName())
        add_enemy(enemies, shadow_creature.getName())
        combat(enemies, shadow_creature, player)
        max_items(items, player)
        door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
        # If you choose 1
        if door_choice == 1:
            door_code(door_choice, 1, shadow_creature, player, enemies, items)
            door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
            # If you choose 1, 1
            if door_choice == 1:
                door_code(door_choice, 2, shadow_creature, player, enemies, items)
                door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
                # If you choose 1, 1, 1
                if door_choice == 1:
                    door_code(door_choice, 3, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
                # If you choose 1, 1, 2
                elif door_choice == 2:
                    door_code(door_choice, 2, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
            # If you choose 1, 2
            elif door_choice == 2:
                door_code(door_choice, 1, shadow_creature, player, enemies, items)
                door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
                # If you choose 1, 2, 1
                if door_choice == 1:
                    door_code(door_choice, 2, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
                # If you choose 1, 2, 2
                elif door_choice == 2:
                    door_code(door_choice, 2, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
        # If you choose 2
        elif door_choice == 2:
            door_code(door_choice, 3, shadow_creature, player, enemies, items)
            door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
            # If you choose 2, 1
            if door_choice == 1:
                door_code(door_choice, 2, shadow_creature, player, enemies, items)
                door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
                # If you choose 2, 1, 1
                if door_choice == 1:
                    door_code(door_choice, 1, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
                # If you choose 2, 1, 2
                elif door_choice == 2:
                    door_code(door_choice, 1, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
            elif door_choice == 2:
                door_code(door_choice, 3, shadow_creature, player, enemies, items)
                door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
                # If you choose 2, 2, 1
                if door_choice == 1:
                    door_code(door_choice, 1, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
                # If you choose 2, 2, 2
                elif door_choice == 2:
                    door_code(door_choice, 2, shadow_creature, player, enemies, items)
                    final_door_fight(player, the_forest_shadow, enemies)
    
    #Back route
    elif temple_path_choice == "Back":
        slow_text(f"{player.getName()} walks around and finds a back entrance")
        slow_text("Thanks to taking the back entance you get straight to")
        slow_text("The Final Boss: The Forest Shadow")
        add_enemy(enemies, the_forest_shadow.getName())
        combat(enemies, the_forest_shadow, player)
        slow_text(f"When {player.getName()} defeats The Forest Shadow the temple start to crumble")
        slow_text("Thanks to taking the back exit you manage to flee")
        slow_text("You return to the village where you tell the story of what has happened")
        slow_text(f"The story of {player.getName()} is told for decades to come")
        slow_text("The end                                                     ....or is it?")
        credits()

# If you choose to explore
elif camp_choice == "Explore":
    slow_text("I am going to try to find out what is in this forest")
    slow_text("You find an item on the ground")
    max_items(items, player)
    slow_text("You can hear some rumbling in the bushes")
    slow_text("Suddenly a forest beast jumps out from the bushes")
    add_enemy(enemies, forest_beast.getName())
    combat(enemies, forest_beast, player)
    slow_text("That was close")
    slow_text("This forest is just it was in the stories")
    slow_text(f"While {player.getName()} was exploring the forest he found and unknown person")
    slow_text("The person introduces themselves as Bartolomeus")
    slow_text("Bartolomeus said he had previously explored the forest")
    slow_text("He said had failed to defeat the evil but manages to flee and now lives in the forest")
    slow_text("Bartolomeus tells you about a temple in the middle of the forest that houses a monster named The Forest Shadow")
    slow_text("He gives you an item")
    max_items(items, player)
    slow_text("Bartolomeus tells you that the shadows creature are part of the forest shadows power")

    bart_choice = inquirer_input(slow_text("Do you trust Bartolomeus?"), ["Yes", "No"])

    #If you trust bartolomeus(dark ending)