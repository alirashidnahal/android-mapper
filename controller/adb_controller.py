import subprocess

def tap_on_screen(x, y):
    subprocess.run(["adb", "shell", "input", "tap", str(x), str(y)])
