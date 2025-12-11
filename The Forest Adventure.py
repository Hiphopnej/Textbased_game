# Import all of the files
from text_functions import inquirer_input
from text_functions import slow_text
from text_functions import slower_text
from classes import Charachter
from classes import Player
from combat_functions import combat
from combat_functions import max_items
from other_functions import door_code
from other_functions import final_door_fight
from other_functions import game_credits

# main

# lists
enemies = []
items = []
play_again = "Yes"

player_name = input("Enter your name ")

# Create all objects
player = Player(200, 20, 90, 10, 60, 90, player_name, items)
forest_beast = Charachter(100, 10, 195, 5, 10, 20, "Forest Beast")
shadow_creature = Charachter(125, 30, 50, 10, 20, 30, "Shadow Creature")
the_forest_shadow = Charachter(150, 50, 70, 10, 30, 40, "The Final Boss: The Forest Shadow")
# Hard mode objects
forest_beast_hard = Charachter(75, 15, 30, 10, 15, 30, "Forest Beast")
shadow_creature_hard = Charachter(150, 45, 75, 15, 35, 50, "Shadow Creature")
the_forest_shadow_hard = Charachter(200, 50, 80, 10 ,45, 60, "The Final Boss: The Forest Shadow")
# Hardest boss in the game
true_final_boss = Charachter(225, 50, 85, 15 ,40, 50, "The True Final Boss: Bartolomeus")
true_final_boss_revived = Charachter(325, 50, 90, 15 ,50, 70, "The Revived True Final Boss: Bartolomeus")
#Exists just for getName()
final_boss = Charachter(225, 50, 85, 15 ,40, 50, "Bartolomeus")

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

while play_again == "Yes":
    # The game begins
    slow_text("There once was a mysterious forest")
    slow_text("It was dim and quiet and all who lived in the nearby village was telling scary stories about it")
    slow_text(f"One day {player.getName()} decided to try to investigate the mystery surrounding the forest so that no one has to be afraid anymore")
    slow_text(f"{player.getName()} takes his sword and enters the forest")
    slow_text("I wonder what can be so mysterious about this forest")
    camp_choice = inquirer_input(slow_text("Should I first put up a camp or should I continue exploring?"), ["Camp", "Explore"])

    # Camp route
    if camp_choice == "Camp":
        slow_text("I should probably put up a camp first")
        slow_text("What is this?")
        max_items(items, player)
        slow_text(f"{player.getName()} was getting ready to sleep when suddenly")
        slow_text("A forest beast appears")
        # Your very first fight
        message = combat(enemies, forest_beast, player, items, 1)
        if message == "you died":
            play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
            continue
        slow_text("That was close, hope it's safe to sleep now")
        slow_text("--------------------------------------------------------")
        slow_text("The next day")
        slow_text("--------------------------------------------------------")
        slow_text("I need to find out where the monster came from")
        slow_text("I should try to get to the middle of the forest")
        slow_text(f"When {player.getName()} gets farther in he finds a shadow creature")
        message = combat(enemies, shadow_creature, player, items, 1)
        if message == "you died":
            play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
            continue
        slow_text("That shadow creature was stronger than that forest beast")
        slow_text("It must be related to the mystery")
        slow_text(f"When {player.getName()} get to the middle of the forest, he discovers a temple")
        slow_text(f"This temple must be related to the evil of this forest")
        temple_path_choice = inquirer_input(slow_text("Should I try to find a path around or just go in at the front?"), ["Front", "Back"])

        # Front route
        if temple_path_choice == "Front":
            slow_text(f"When {player.getName()} enters the temple he encounters two shadow creatures")
            message = combat(enemies, shadow_creature, player, items, 2)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            
            #The door path begins
            slow_text(f"When {player.getName()} enters the temple he encounters two shadow creatures")
            message = combat(enemies, shadow_creature, player, items, 2)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
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
                        inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                        continue
                    # If you choose 1, 1, 2
                    elif door_choice == 2:
                        door_code(door_choice, 2, shadow_creature, player, enemies, items)
                        final_door_fight(player, the_forest_shadow, enemies)
                        inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                        continue
                # If you choose 1, 2
                elif door_choice == 2:
                    door_code(door_choice, 1, shadow_creature, player, enemies, items)
                    door_choice = inquirer_input(slow_text("There are two doors in fornt of you"), ["1", "2"])
                    # If you choose 1, 2, 1
                    if door_choice == 1:
                        door_code(door_choice, 2, shadow_creature, player, enemies, items)
                        final_door_fight(player, the_forest_shadow, enemies)
                        inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                        continue
                    # If you choose 1, 2, 2
                    elif door_choice == 2:
                        door_code(door_choice, 2, shadow_creature, player, enemies, items)
                        final_door_fight(player, the_forest_shadow, enemies)
                        inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                        continue
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
                        inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                        continue
                    # If you choose 2, 1, 2
                    elif door_choice == 2:
                        door_code(door_choice, 1, shadow_creature, player, enemies, items)
                        final_door_fight(player, the_forest_shadow, enemies)
                        inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                        continue
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
            slower_text("The Final Boss: The Forest Shadow")
            
            if "Godslayer" in items:
                items.remove("Godslayer")

            message = combat(enemies, the_forest_shadow, player, items, 1)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            slow_text(f"When {player.getName()} defeats The Forest Shadow the temple start to crumble")
            slow_text("Thanks to taking the back exit you manage to flee")
            slow_text("You return to the village where you tell the story of what has happened")
            slow_text(f"The story of {player.getName()} is told for decades to come")
            slower_text("The end        ....or is it?")
            game_credits()
            inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
            continue

    # If you choose to explore
    elif camp_choice == "Explore":
        slow_text("I am going to try to find out what is in this forest")
        slow_text("You find an item on the ground")
        max_items(items, player)
        slow_text("You can hear some rumbling in the bushes")
        slow_text("Suddenly a forest beast jumps out from the bushes")
        message = combat(enemies, forest_beast, player, items, 1)
        if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
        slow_text("That was close")
        slow_text("This forest is just like it was in the stories")
        slow_text(f"While {player.getName()} was exploring the forest he found an unknown person")
        slow_text(f"The person introduces themselves as {final_boss.getName()}")
        slow_text(f"{final_boss.getName()} said he had previously explored the forest")
        slow_text("He said had failed to defeat the evil but manages to flee and now lives in the forest")
        slow_text(f"{final_boss.getName()} tells you about a temple in the middle of the forest that houses a monster named The Forest Shadow")
        slow_text("He gives you an item")
        max_items(items, player)
        slow_text(f"{final_boss.getName()} tells you that the shadows creature are part of the forest shadows power")

        trust_choice = inquirer_input(slow_text(f"Do you trust {final_boss.getName()}?"), ["Yes", "No"])

        #If you trust the true final boss(dark ending)
        if trust_choice == "Yes":
            slow_text(f"{final_boss.getName()} thanks {player.getName()} for trusting him")
            slow_text("He then takes you to his cabin where you decide to stay for the night")
            slow_text(f"{final_boss.getName()} also gives you another item")
            max_items(items, player)
            slow_text(f"You get a feeling that {final_boss.getName()} is a bit to nice")
            slow_text("--------------------------------------------------------")
            slow_text("The next day")
            slow_text("--------------------------------------------------------")
            slow_text(f"{player.getName()} and {final_boss.getName()} goes to the temple where a shadow creature appears")
            message = combat(enemies, shadow_creature_hard, player, items, 1)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            slow_text(f"{player.getName()} felt like the {shadow_creature_hard.getName()} was stronger than normal")
            slow_text(f"{final_boss.getName()} tells you that there is a back entrance you should take")
            slow_text("As you approch it two shadow creatures appears")
            message = combat(enemies, shadow_creature_hard, player, items, 2)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            slow_text(f"When {player.getName()} gets to the final room he finds")
            slow_text(f"{the_forest_shadow_hard.getName()}")

            if "Godslayer" in items:
                items.remove("Godslayer")

            message = combat(enemies, the_forest_shadow_hard, player, items, 1)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            slow_text("When you defeat the forest shadow you can feel something though your chest")
            slower_text(f"{final_boss.getName()} had stabbed you from behind")
            slower_text(f"{player.getName()} knew there was something off with him")
            slower_text(f"{final_boss.getName()} tells you how he made the enemys stronger")
            slower_text(f"In your last breath you see {final_boss.getName()} revive the forest shadow")
            slower_text(f"The mystery of the forest continue and no one remebers {player.getName()}")
            slower_text("The End")
            game_credits()
            inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
            continue

        elif trust_choice == "No":
            slow_text(f"{player.getName()} decides not to trust {final_boss.getName()} probably the best choice")
            slow_text("You continue to explore the forest")
            slow_text(f"{player.getName()} goes to the middle of the forest but from the shadows behind you a shadow creature appears")

            message = combat(enemies, shadow_creature, player, items, 1)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            slow_text(f"{player.getName()} defeats the shadow creature")
            slow_text(f"After a while {player.getName()} finally reaches the temple")
            slow_text(f"When he enters the temple he encounters three shadow creatures")
            message = combat(enemies, shadow_creature, player, items, 3)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            if "Godslayer" in items:
                items.remove("Godslayer")
            slow_text(f"After defeating the shadow creatures you get to the middle of temple and there you find {final_boss.getName()}?????")
            slow_text(f"{final_boss.getName()} tells you that it was smart not to trust him but that you are going to have to pay for ruining his plans")
            message = combat(enemies, true_final_boss, player, items, 1)
            if message == "you died":
                play_again = inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            slower_text(f"After seemingly deafeating {final_boss.getName()} his power start seeping out of him and he says")
            slower_text("It's not over yet")
            dead_or_not = combat(enemies, true_final_boss_revived, player, items, 1)
            # Evil ending
            if dead_or_not == "player died to final boss":
                slower_text(f"{final_boss.getName()} power start taking over you")
                slow_text(f"{final_boss.getName()} disappears and {player.getName()} feels that he must spread the evil")
                slower_text(f"You have become the Forest Shadow")
                slow_text(f"{player.getName()} continues to spread evil and destroys the village")
                slower_text("The end")
                game_credits()
                inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue
            
            #True ending
            else:
                slow_text(f"After finally deafeating {final_boss.getName()} his power disappears as he screams nooooooooooooooooooooooooooooooooo!!!!!!")
                slow_text(f"You leave the temple as it explodes behind you")
                slow_text(f"The story of {player.getName()} is told for decades to come")
                slower_text("The True Ending")
                slow_text("Message from the developer")
                slow_text("Congratulations for getting the true ending")
                slow_text("If you have managed to get to this point without using godslayer you have managed to pull off something truly impressive")
                slow_text("I hope you had fun playing it")
                slow_text("Thank you")
                inquirer_input(slow_text("Do you want to play again"), ["Yes", "No"])
                continue