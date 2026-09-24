import os

def show_files():

    files = os.listdir()

    for file in files:
        print(file)