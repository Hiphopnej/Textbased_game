from InquirerPy import inquirer
import time

def inquirer_input(message_param, options):
    choice = inquirer.select(
        message=message_param,
        choices = options
    ).execute()
    return choice

# wait time is 0.04 for normal text
# and 0.1 for intense text

def slow_text(message, wait_time):
    message += "\n"
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(wait_time)