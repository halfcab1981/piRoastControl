import logging
import os
import time
import RPi.GPIO as GPIO
from zero_cross import setup_zero_cross_detection, cleanup_gpio as cleanup_zero_cross
from heat_control import setup_heat_control, trigger_heat, cleanup_gpio as cleanup_heat
from fan_control import setup_fan_control, set_fan_speed, cleanup_gpio as cleanup_fan

# Set up the correct path for the log file
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
log_file = os.path.join(log_dir, 'system.log')

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting piRoastControl system")
    
    try:
        setup_zero_cross_detection()
        setup_heat_control()
        fan_pwm = setup_fan_control()
        
        # Main control loop
        heat_power = 50  # Start at 50% power
        fan_speed = 50   # Start at 50% speed
        while True:
            trigger_heat(heat_power)
            set_fan_speed(fan_pwm, fan_speed)
            time.sleep(0.1)  # Wait for 100ms before next cycle
    
    except KeyboardInterrupt:
        logging.info("System shutdown initiated by user")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        cleanup_zero_cross()
        cleanup_heat()
        cleanup_fan(fan_pwm)
        logging.info("System shutdown complete")

if __name__ == "__main__":
    main()
