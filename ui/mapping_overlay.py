from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtCore import Qt, QPoint
import json
import sys

class MappingOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تعریف مپینگ")
        self.setGeometry(100, 100, 720, 1280)  # ابعاد دلخواه (یا شبیه به scrcpy)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: rgba(0, 0, 0, 80);")  # نیمه شفاف

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos: QPoint = event.pos()
            x = pos.x()
            y = pos.y()
            key, ok = QInputDialog.getText(self, "ورود کلید", f"کدام کلید برای مختصات ({x},{y})؟")
            if ok and key:
                self.save_mapping(key.lower(), x, y)
                print(f"✅ {key} → ({x},{y}) ذخیره شد.")

    def save_mapping(self, key, x, y):
        try:
            with open("config/mappings.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data[key] = [x, y]
        with open("config/mappings.json", "w") as f:
            json.dump(data, f, indent=4)

def start_overlay():
    app = QApplication(sys.argv)
    window = MappingOverlay()
    window.show()
    sys.exit(app.exec_())
