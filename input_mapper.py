import threading
import keyboard
import subprocess
from utils.mapping_manager import MappingManager
from typing import Dict, List

class InputMapper:
    def __init__(self, game_id: str = "default"):
        self.mapping_manager = MappingManager()
        self.mappings = self.mapping_manager.get_mappings(game_id)
        self.running = False

    def tap_on_phone(self, x: int, y: int) -> None:
        """ارسال فرمان تاچ به دستگاه"""
        cmd = f"adb shell input tap {x} {y}"
        try:
            subprocess.run(cmd, shell=True)
            print(f"👉 Touch on ({x}, {y})")
        except Exception as e:
            print(f"❌ Error executing ADB: {e}")

    def _on_key_press(self, key: str) -> None:
        """مدیریت فشار کلید"""
        if key in self.mappings:
            x, y = self.mappings[key]
            self.tap_on_phone(x, y)

    def start(self) -> None:
        """شروع گوش دادن به کلیدها"""
        if not self.mappings:
            print("❗ No mappings found. Run '--mapping' first.")
            return

        print("🎮 Run mode is enabled. Press Ctrl+C to exit.")
        self.running = True

        # ثبت کلیدهای hotkey
        for key in self.mappings:
            keyboard.add_hotkey(key, lambda k=key: self._on_key_press(k))

        # نگه داشتن برنامه
        try:
            threading.Event().wait()
        except KeyboardInterrupt:
            self.stop()

    def stop(self) -> None:
        """توقف گوش دادن به کلیدها"""
        if self.running:
            keyboard.unhook_all()
            self.running = False
            print("🛑 Input mapper stopped.")
