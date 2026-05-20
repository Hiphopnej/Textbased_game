# Import all of the files
from text_functions import inquirer_input, slow_text
from other_functions import create_charachter
from story_functions import start_story
from save_functions import load_game
from classes import Player
import os
import os.path

# main

play_again = "Yes"
enemies = []

while play_again == "Yes":
    save_choice = inquirer_input(slow_text("Welcome to The Forest Adventure", 0.04), ["New save", "Continue"])

    if save_choice == "New save":
        player = create_charachter()
        start_story(player, enemies)
    elif save_choice == "Continue":
        # Get all of the files in the saves folder
        onlyfiles = [f for f in os.listdir("saves/") if os.path.isfile(os.path.join("saves/", f))]
        if onlyfiles == []:
            slow_text("No save file found", 0.04)
            continue
        else:
            # Makes it so .json doesn't get displayed
            filemap = {f.replace(".json", ""): f for f in onlyfiles}

            player_choice = inquirer_input(slow_text("Choose a player", 0.04), list(filemap.keys()))

            player_name = filemap[player_choice]
        # Loads game
        save_data = load_game(player_name)
        save_data = save_data[0]
        if save_data is None:
            slow_text("No save file found")
            continue
        player = Player.from_save(save_data)
        chapter = save_data["current_chapter"]
        play_again = start_story(player, enemies, start_at=chapter)

    # List of all objects
    """
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
    """