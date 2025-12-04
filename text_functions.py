from InquirerPy import inquirer
import time

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