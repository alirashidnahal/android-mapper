from ui.main_window import launch_ui
from listener.keyboard_listener import start_listener
from ui.mapping_overlay import start_overlay
import threading
import sys

if __name__ == "__main__":
    if "--mapping" in sys.argv:
        start_overlay()
    else:
        listener_thread = threading.Thread(target=start_listener, daemon=True)
        listener_thread.start()
        launch_ui()
