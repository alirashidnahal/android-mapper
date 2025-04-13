import argparse
import subprocess
from input_mapper import listen_for_keys

def start_scrcpy():
    try:
        subprocess.Popen(["scrcpy"])
        print("📱 scrcpy was run.")
    except FileNotFoundError:
        print("❌ scrcpy is not installed or is not in the PATH. Please install it first.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mapping", action="store_true", help="define custom key mappings")
    args = parser.parse_args()

    if args.mapping:
        from ui.mapping_overlay import start_overlay
        start_overlay()
    else:
        start_scrcpy()
        listen_for_keys()

if __name__ == "__main__":
    main()
