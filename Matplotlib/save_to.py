import os

SAVE_DIR = f"{os.getcwd()}\\figures"

def get_dir():
    if not os.path.exists(SAVE_DIR):
        os.mkdir(SAVE_DIR)
    return SAVE_DIR
