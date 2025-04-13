from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import subprocess
import sys
import os

def launch_ui():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Android USB Mapper")
    layout = QVBoxLayout()

    label = QLabel("برای اتصال گوشی، روی دکمه کلیک کن")
    layout.addWidget(label)

    connect_btn = QPushButton("اتصال به گوشی (start scrcpy)")
    layout.addWidget(connect_btn)

    def start_scrcpy():
        try:
            subprocess.Popen(["scrcpy"])
            label.setText("در حال اتصال...")
        except FileNotFoundError:
            label.setText("❌ scrcpy نصب نیست یا در مسیر سیستم قرار نگرفته.")

    connect_btn.clicked.connect(start_scrcpy)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
