import argparse
import subprocess
from input_mapper import InputMapper
from ui.mapping_overlay import start_overlay

def start_scrcpy() -> None:
    """اجرای scrcpy"""
    try:
        subprocess.Popen(["scrcpy"])
        print("📱 scrcpy was run.")
    except FileNotFoundError:
        print("❌ scrcpy is not installed or is not in the PATH. Please install it first.")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Android Input Mapper - Map keyboard inputs to screen coordinates"
    )
    parser.add_argument(
        "--mapping", 
        action="store_true", 
        help="define custom key mappings"
    )
    parser.add_argument(
        "--game",
        type=str,
        default="default",
        help="game ID to use mappings for"
    )
    
    args = parser.parse_args()

    if args.mapping:
        start_overlay()
    else:
        start_scrcpy()
        mapper = InputMapper(args.game)
        mapper.start()

if __name__ == "__main__":
    main()
