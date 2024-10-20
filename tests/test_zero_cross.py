from gpiozero import Button
from signal import pause
import json
import os

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'settings.json')
with open(config_path, 'r') as config_file:
    settings = json.load(config_file)

ZERO_CROSS_PIN = settings['zero_cross_pin']

def zero_cross_callback():
    print("Zero-cross detected!")

def main():
    zero_cross = Button(ZERO_CROSS_PIN, pull_up=False)
    zero_cross.when_pressed = zero_cross_callback

    print(f"Monitoring zero-cross events on GPIO {ZERO_CROSS_PIN}. Press Ctrl+C to exit.")
    
    try:
        pause()
    except KeyboardInterrupt:
        print("Test ended by user.")

if __name__ == "__main__":
    main()