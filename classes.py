import random
from text_functions import inquirer_input
from text_functions import slow_text

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

    def setHealth(self):
        self.health = 200

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
            inventory_length = len(self.inventory)
            match inventory_length:
                case 1:
                    chosen_item = inquirer_input(f"What item do you want to use: {self.inventory}", [self.inventory[0]])
                case 2:
                    chosen_item = inquirer_input(f"What item do you want to use: {self.inventory}", [self.inventory[0], self.inventory[1]])
                case 3:
                    chosen_item = inquirer_input(f"What item do you want to use: {self.inventory}", [self.inventory[0], self.inventory[1], self.inventory[2]])
                case 4:
                    chosen_item = inquirer_input(f"What item do you want to use: {self.inventory}", [self.inventory[0], self.inventory[1], self.inventory[2], self.inventory[3]])
                case 5:
                    chosen_item = inquirer_input(f"What item do you want to use: {self.inventory}", [self.inventory[0], self.inventory[1], self.inventory[2], self.inventory[3], self.inventory[4]])
            if chosen_item == "ecologic egg launcher":
                enemy_object.take_damage(1)
                slow_text(f"{enemy_object.name} took 1 dmg")
            elif chosen_item == "godslayer":
                enemy_object.take_damage(1000000000000)
                slow_text(f"{enemy_object.name} took 1000000000000 dmg")
            elif chosen_item == "attack brew":
                enemy_object.take_damage(80)
                slow_text(f"{enemy_object.name} took 80 dmg")
                self.inventory.remove("attack brew")
            elif chosen_item == "health brew":
                self.health += 100
                slow_text(f"You healed 100hp and now your total hp is {self.health}")
                self.inventory.remove("health brew")