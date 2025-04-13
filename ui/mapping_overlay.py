import json
import sys
import time
import pygetwindow as gw
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor

mapping = {}

# لیست کلیدهایی که می‌خوایم مپ کنیم
keys_to_map = ['A', 'S', 'D', 'W']
current_key_index = 0

def get_scrcpy_geometry():
    """مکان و ابعاد پنجره scrcpy را برمی‌گرداند"""
    time.sleep(1)  # صبر برای باز شدن پنجره
    for w in gw.getWindowsWithTitle('scrcpy'):
        if w.visible:
            return w.left, w.top, w.width, w.height
    return None

class TransparentOverlay(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        geometry = get_scrcpy_geometry()
        if geometry:
            x, y, w, h = geometry
            self.setGeometry(x, y, w, h)
            print(f"📐 Scrcpy window detected: ({x},{y},{w},{h})")
        else:
            print("❗ Scrcpy window not found, using default size.")
            self.setGeometry(100, 100, 800, 600)

        self.setMouseTracking(True)
        self.setCursor(Qt.CrossCursor)

    def mousePressEvent(self, event):
        global current_key_index

        if current_key_index >= len(keys_to_map):
            return

        if event.button() == Qt.LeftButton:
            pos = event.pos()
            key = keys_to_map[current_key_index]
            mapping[key] = {"x": pos.x(), "y": pos.y()}
            print(f"🎯 Position for the key '{key}': {mapping[key]}")
            current_key_index += 1

            if current_key_index >= len(keys_to_map):
                with open("mapping.json", "w") as f:
                    json.dump(mapping, f, indent=4)
                print("✅ mapping.json saved.")
                self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        color = QColor(255, 255, 255, 40)  # سفید شفاف
        painter.fillRect(self.rect(), color)

def start_overlay():
    app = QApplication(sys.argv)
    window = TransparentOverlay()
    window.show()
    sys.exit(app.exec_())
