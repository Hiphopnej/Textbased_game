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

def slow_text(message):
    message += "\n"
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(0.03)

class Charachter:
    #Initiate all varibles
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
        #Calulate dmg
        dmg = random.randint(self.dmgLower, self.dmgHigher)

        #Calculate crit
        crit = random.randint(1,20)

        #Calculate total damage
        total_dmg = self.base_dmg + dmg

        #Deals dmg based on if critted or not
        if crit == 11:
            crit_dmg = total_dmg * 1.5
            enemy_object.take_damage(crit_dmg)
            slow_text(f"You got a crit and dealt {crit_dmg} to {enemy_object.name}")
        else:
            enemy_object.take_damage(total_dmg)
            slow_text(f"{enemy_object.name} took {total_dmg} amount of dmg")
    
    def heal(self):
        #Calculate heal amount
        heal_amount = random.randint(self.healingLower, self.healingHigher)

        #Heal
        self.health += heal_amount
        slow_text(f"{self.name} healed {heal_amount}hp and now thier total hp is: {self.health}hp")

    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health

#Player class that inherits from Charachter class
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
            chosen_item = inquirer.select(
                message=f"What item do you want to use: {self.inventory}",
                #Not sure if this works
                choices = [self.inventory]
            ).execute()
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

#Credits
def credits():
    slow_text("Code by Alvar Eklind")
    slow_text("Story by Alvar Eklind")
    slow_text("Thanks for playing and hope you enjoyed yourself")

#Combat function
def combat(enemies, enemy_object, player_object):
    #For loop to allow for double battles
    for enemy in enemies:
        print("--------------------------------------------------------")
        
        #Add random intros to the battles
        intro = random.randint(1,3)
        match intro:
            case 1:
                slow_text(f"A {enemy_object.getName()} has appeared")
            case 2:
                slow_text(f"You're fighting against a {enemy_object.getName()}")
            case 3:
                slow_text(f"A {enemy_object.getName()} attacks")

        #The battle begins   
        while player_object.getHealth() > 0 and enemy_object.getHealth() > 0:
            #Write out player health and enemy health
            print("--------------------------------------------------------")
            slow_text(f"You have {player_object.getHealth()}hp and {enemy_object.getName()} has {enemy_object.getHealth()}hp")
            print("--------------------------------------------------------")
            start_first = random.randint(1,2)
            if start_first == 1:
                slow_text(f"{player_object.getHealth()} is faster than you")
                #Choose a attack for the enemy
                attack_chosen = random.randint(1,2)
                if attack_chosen == 1:
                    enemy_object.attack(player_object)
                    if player_object.getHealth() <= 0:
                        slow_text("You died")
                        exit()
                elif attack_chosen == 2:
                    enemy_object.heal()
                move_choice = inquirer.select(
                    message="What do you want to do?",
                    choices = ["Attack", "Heal", "Item"]
                ).execute()
                if move_choice.lower() == "attack":
                    player_object.attack(enemy_object)
                    if enemy_object.getHealth <= 0:
                        slow_text("You this battle")
                        break
                elif move_choice.lower() == "heal":
                    player_object.heal()
                elif move_choice.lower() == "item":
                    player_object.use_item(enemy_object)
            elif start_first == 2:
                # Your attack
                move_choice = inquirer.select(
                    message="What do you want to do?",
                    choices = ["Attack", "Heal", "Item"]
                ).execute()
                if move_choice.lower() == "attack":
                    player_object.attack(enemy_object)
                    if enemy_object.getHealth <= 0:
                        slow_text("You this battle")
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