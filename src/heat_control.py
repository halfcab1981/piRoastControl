import sys
import typing
from time import sleep
import logging

if typing.TYPE_CHECKING:
    from gpiozero import OutputDevice
else:
    OutputDevice = typing.Any

try:
    from gpiozero import OutputDevice
except ImportError:
    from gpio_mock import OutputDevice


class HeatControl:
    def __init__(self, pin):
        self.heat_pin = OutputDevice(pin)
        self.power_level = 0

    def set_power(self, power_level):
        self.power_level = max(0, min(100, power_level))

    def trigger(self):
        if self.power_level > 0:
            self.heat_pin.on()
            sleep(self.power_level / 2000)  # Convert percentage to milliseconds
            self.heat_pin.off()

def setup_heat_control(pin):
    logging.info("Setting up heat control")
    return HeatControl(pin)
