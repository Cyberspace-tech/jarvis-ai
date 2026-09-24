import os

def execute(command):

    command = command.lower()

    if "notepad" in command:
        os.system("notepad")

    elif "calculator" in command:
        os.system("calc")

    elif "chrome" in command:
        os.system("start chrome")