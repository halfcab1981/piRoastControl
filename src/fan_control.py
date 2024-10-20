import sys
import typing
import logging

# Type checking imports
if typing.TYPE_CHECKING:
    from gpiozero import PWMOutputDevice
else:
    PWMOutputDevice = typing.Any

# Try to import the actual PWMOutputDevice, fall back to mock if not available
try:
    from gpiozero import PWMOutputDevice
except ImportError:
    from gpio_mock import PWMOutputDevice

class FanControl:
    def __init__(self, pin):
        # Initialize the PWM output for the fan
        # The frequency of 100 Hz is typical for many PWM applications
        self.fan_pin = PWMOutputDevice(pin, frequency=100)
        self.speed = 0
        
        # Define the fan settings
        # The key is the fan setting (0-8)
        # The value is the duty cycle percentage
        # Note: Higher duty cycle means lower fan speed due to inverted control
        self.fan_settings = {
            0: 100,  # 0% fan power (100% duty cycle)
            1: 65,   # Setting 1
            2: 62,   # Setting 2
            3: 58,   # Setting 3
            4: 54,   # Setting 4
            5: 54,   # Setting 5
            6: 50,   # Setting 6
            7: 45,   # Setting 7
            8: 0     # Setting 8 (max fan power, 0% duty cycle)
        }

    def set_speed(self, speed_setting):
        # Validate the input speed setting
        if speed_setting not in self.fan_settings:
            raise ValueError(f"Invalid fan speed setting: {speed_setting}")
        
        # Get the duty cycle for the given speed setting
        duty_cycle = self.fan_settings[speed_setting]
        
        # Set the PWM duty cycle (value between 0 and 1)
        self.fan_pin.value = duty_cycle / 100
        
        # Update the current speed setting
        self.speed = speed_setting
        
        # Log the speed change
        logging.info(f"Fan speed set to {speed_setting} (duty cycle: {duty_cycle}%)")

def setup_fan_control(pin):
    logging.info("Setting up fan control")
    return FanControl(pin)

def cleanup_gpio():
    # This function will clean up the GPIO pins
    logging.info("Cleaning up GPIO pins")
    # If using gpiozero, it automatically cleans up on exit
    # If using RPi.GPIO, you might need to add: GPIO.cleanup()
