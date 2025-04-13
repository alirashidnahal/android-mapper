from ui.main_window import launch_ui
from listener.keyboard_listener import start_listener
import threading

if __name__ == "__main__":
    # اجرا به صورت دو نخ موازی: یکی برای UI و یکی برای لیسنر
    listener_thread = threading.Thread(target=start_listener, daemon=True)
    listener_thread.start()

    launch_ui()
