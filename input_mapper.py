import json
import os
import threading
import keyboard
import subprocess

MAPPING_PATH = "config/mappings.json"

def load_mappings():
    if not os.path.exists(MAPPING_PATH):
        print("❗ فایل مپینگ پیدا نشد. ابتدا '--mapping' اجرا کن.")
        return {}
    with open(MAPPING_PATH, "r") as f:
        return json.load(f)

def tap_on_phone(x, y):
    cmd = f"adb shell input tap {x} {y}"
    try:
        subprocess.run(cmd, shell=True)
        print(f"👉 تاچ در ({x}, {y})")
    except Exception as e:
        print(f"❌ خطا در اجرای ADB: {e}")

def listen_for_keys():
    mappings = load_mappings()
    if not mappings:
        return

    print("🎮 حالت اجرا فعال شد. برای خروج Ctrl+C بزن.")
    for key in mappings:
        keyboard.add_hotkey(key, lambda x=mappings[key]: tap_on_phone(x[0], x[1]))

    # نگه داشتن برنامه
    threading.Event().wait()
