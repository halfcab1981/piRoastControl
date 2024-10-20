import sys
import typing
import logging

if typing.TYPE_CHECKING:
    from gpiozero import PWMOutputDevice
else:
    PWMOutputDevice = typing.Any

try:
    from gpiozero import PWMOutputDevice
except ImportError:
    from gpio_mock import PWMOutputDevice


class FanControl:
    def __init__(self, pin):
        self.fan_pin = PWMOutputDevice(pin, frequency=100)
        self.speed = 0
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
        if speed_setting not in self.fan_settings:
            raise ValueError(f"Invalid fan speed setting: {speed_setting}")
        duty_cycle = self.fan_settings[speed_setting]
        self.fan_pin.value = duty_cycle / 100
        self.speed = speed_setting
        logging.info(f"Fan speed set to {speed_setting} (duty cycle: {duty_cycle}%)")

def setup_fan_control(pin):
    logging.info("Setting up fan control")
    return FanControl(pin)
