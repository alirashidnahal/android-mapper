import argparse
import subprocess
from input_mapper import listen_for_keys

def start_scrcpy():
    try:
        subprocess.Popen(["scrcpy"])
        print("📱 scrcpy اجرا شد.")
    except FileNotFoundError:
        print("❌ scrcpy نصب نیست یا در PATH نیست. لطفاً نصب کن.")

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
