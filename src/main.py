import logging
import os
import time
import json
from fan_control import setup_fan_control

# Try to import cleanup_gpio, but don't fail if it's not available
try:
    from fan_control import cleanup_gpio as cleanup_fan
except ImportError:
    cleanup_fan = lambda: None  # Define a no-op function if cleanup_gpio is not available

# Set up the correct paths for log file and config file
base_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(base_dir, 'logs')
log_file = os.path.join(log_dir, 'system.log')
config_file = os.path.join(base_dir, 'config', 'settings.json')

# Configure logging
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    # Load and return the configuration from the JSON file
    with open(config_file, 'r') as f:
        return json.load(f)

def main():
    logging.info("Starting fan control test")
    
    try:
        # Load the configuration
        config = load_config()
        
        # Set up the fan control using the pin specified in the config
        fan_control = setup_fan_control(config['fan_pin'])
        
        # Test each fan speed setting
        for speed in range(9):  # 0 to 8
            fan_control.set_speed(speed)
            print(f"Setting fan speed to {speed}")  # Print current speed to console
            time.sleep(5)  # Run each speed for 5 seconds
    
    except KeyboardInterrupt:
        print("\nTest shutdown initiated by user")
        logging.info("Test shutdown initiated by user")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        # Call cleanup_fan, which will be a no-op if cleanup_gpio was not imported
        cleanup_fan()
        print("Fan control test complete")
        logging.info("Fan control test complete")

if __name__ == "__main__":
    main()
