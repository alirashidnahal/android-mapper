import json
from controller.adb_controller import tap_on_screen

with open("config/mappings.json", "r") as f:
    mappings = json.load(f)

def handle_key_press(key):
    if key in mappings:
        x, y = mappings[key]
        tap_on_screen(x, y)
