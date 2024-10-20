import logging
import os
import time
import json
from fan_control import setup_fan_control, cleanup_gpio as cleanup_fan

# Set up the correct path for the log file and config file
base_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(base_dir, 'logs')
log_file = os.path.join(log_dir, 'system.log')
config_file = os.path.join(base_dir, 'config', 'settings.json')

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open(config_file, 'r') as f:
        return json.load(f)

def main():
    logging.info("Starting fan control test")
    
    try:
        config = load_config()
        fan_control = setup_fan_control(config['fan_pin'])
        
        # Test each fan speed setting
        for speed in range(9):
            fan_control.set_speed(speed)
            time.sleep(5)  # Run each speed for 5 seconds
    
    except KeyboardInterrupt:
        logging.info("Test shutdown initiated by user")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        cleanup_fan()
        logging.info("Fan control test complete")

if __name__ == "__main__":
    main()
