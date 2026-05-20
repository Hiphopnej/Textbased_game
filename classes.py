import random
from text_functions import inquirer_input, slow_text

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
    
    def setHealth(self, health):
        self.health = health
    
    def attack(self, enemy_object):
        # Calulate dmg
        dmg = random.randint(self.dmgLower, self.dmgHigher)

        # Calculate total damage
        total_dmg = self.base_dmg + dmg
        enemy_object.take_damage(total_dmg)
        slow_text(f"{enemy_object.name} took {total_dmg} amount of dmg", 0.04)
    
    def heal(self):
        # Calculate heal amount
        heal_amount = random.randint(self.healingLower, self.healingHigher)

        # Heal
        self.health += heal_amount
        slow_text(f"{self.name} healed {heal_amount}hp and now their total hp is: {self.health}hp", 0.04)

    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health

# Player class that inherits from Charachter class
class Player(Charachter):
    def __init__(self, name, player_class):
        self.name = name
        self.inventory = []
        self.player_class = player_class
        self.xp = 0
        self.xp_to_next = 100
        self.level = 1
        self.money = 20
        self.godslayer_list = []

        # Classes are Warrior and Mage
        if player_class.lower() == "warrior":
            self.health = 150+(self.level*5)
            self.dmgLower = 3000+(self.level*5)
            self.dmgHigher = 9000+(self.level*5)
            self.base_dmg = 15+(self.level*5)
            self.strength = 10+(self.level*5)
            self.healingLower = 30+(self.level*5)
            self.healingHigher = 60+(self.level*5)
            self.mp = 10+(self.level*5)
            self.magic = 5+(self.level*5)
            self.weapon = "sword"
            self.spells = ["fireball","excalibur"] # excalibur ska göra massvis med damage men kosta jättemycket mp
        elif player_class.lower() == "mage":
            self.health = 175+(self.level*5)
            self.dmgLower = 20+(self.level*5)
            self.dmgHigher = 70+(self.level*5)
            self.base_dmg = 10+(self.level*5)
            self.strength = 5+(self.level*5)
            self.healingLower = 40+(self.level*5)
            self.healingHigher = 70+(self.level*5)
            self.mp = 25+(self.level*5)
            self.magic = 20+(self.level*5)
            self.weapon = "magic staff"
            self.spells = ["fireball", "magic missile", "avalon"] # avalon ska göra så att man gör mer damage och får healing over time men kosta massor med mp

    def attack(self, enemy_object):
        # Calulate dmg
        dmg = random.randint(self.dmgLower, self.dmgHigher)

        # Calculate crit
        crit = random.randint(1,15)

        # Calculate total damage
        total_dmg = self.base_dmg + dmg

        # Deals dmg based on if critted or not
        if crit == 9:
            crit_dmg = total_dmg * 1.5
            enemy_object.take_damage(crit_dmg)
            slow_text(f"You got a crit and dealt {crit_dmg} to {enemy_object.name}", 0.04)
        else:
            enemy_object.take_damage(total_dmg)
            slow_text(f"{enemy_object.name} took {total_dmg} amount of dmg", 0.04)

    def pick_up_item(self):
        item_number = random.randint(1,1000)
        if item_number == 1000:
            self.inventory.append("ecologic egg launcher")
            slow_text("You got a Ecologic egg launcher", 0.04)
        elif item_number >= 989 and item_number < 1000:
            self.inventory.append("godslayer")
            slow_text("You got the Godslayer", 0.04)
        elif item_number >= 0 and item_number <= 495:
            self.inventory.append("attack brew")
            slow_text("You got a attack brew", 0.04)
        else:
            self.inventory.append("health brew")
            slow_text("You got a health brew", 0.04)

    def use_item(self, enemy_object):
        if len(self.inventory) <= 0:
            slow_text("You don't have any items", 0.04)
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
                slow_text(f"{enemy_object.name} took 1 dmg", 0.04)
            elif chosen_item == "godslayer":
                self.godslayer_list.append(enemy_object.getName())

                enemy_object.take_damage(1000000000000)
                slow_text(f"{enemy_object.name} took 1000000000000 dmg", 0.04)
            elif chosen_item == "attack brew":
                enemy_object.take_damage(80)
                slow_text(f"{enemy_object.name} took 80 dmg", 0.04)
                self.inventory.remove("attack brew")
            elif chosen_item == "health brew":
                self.health += 100
                slow_text(f"You healed 100hp and now your total hp is {self.health}", 0.04)
                self.inventory.remove("health brew")
    @staticmethod
    def from_save(data):
        player = Player(data["name"], data["player_class"])
        player.level = data["level"]
        player.xp = data["xp"]
        player.xp_to_next = data["xp_to_next"]
        player.health = data["health"]
        player.mp = data["mp"]
        player.strength = data["strength"]
        player.magic = data["magic"]
        player.weapon = data["weapon"]
        player.spells = data["spells"]
        player.inventory = data["inventory"]
        player.money = data["money"]
        return player