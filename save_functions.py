import json
from pathlib import Path
from text_functions import slow_text

SAVE_FOLDER = Path("saves/")

def save_game(player, current_chapter):
    # Create folder if there doesn't exist one
    SAVE_FOLDER.mkdir(exist_ok=True)

    file_path = SAVE_FOLDER / f"{player.name}.json"

    data = {
        "name": player.name,
        "player_class": player.player_class,
        "level": player.level,
        "xp": player.xp,
        "xp_to_next": player.xp_to_next,
        "health": player.health,
        "mp": player.mp,
        "strength": player.strength,
        "magic": player.magic,
        "weapon": player.weapon,
        "dmgLower": player.dmgLower,
        "dmgHigher": player.dmgHigher,
        "spells": player.spells,
        "inventory": player.inventory,
        "money": player.money,
        "current_chapter": current_chapter
    }

    data_list = [data]

    with open(file_path, "w") as file:
        json.dump(data_list, file)

    slow_text("Game has been saved", 0.04)

def load_game(player_name):
    try:
        file_path = SAVE_FOLDER / f"{player_name}.json"
        with open(file_path, "r") as file:
            data = json.load(file)
            
        return data
    except FileNotFoundError:
        print("File not Found")
        return None