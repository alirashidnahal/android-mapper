from pynput import keyboard
import json
from controller.adb_controller import tap_on_screen

# لود مپینگ کلیدها
def load_mappings():
    try:
        with open("config/mappings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

mappings = load_mappings()

# وقتی کلیدی فشار داده شد
def on_press(key):
    try:
        k = key.char.lower()
        if k in mappings:
            x, y = mappings[k]
            print(f"Pressed {k} → Tapping at {x}, {y}")
            tap_on_screen(x, y)
    except AttributeError:
        pass  # برای کلیدهای خاص مثل shift، ctrl و ...

def start_listener():
    print("🎮 لیسنر فعال شد... برای خروج Ctrl+C بزن")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
