import sys
import typing
import logging

if typing.TYPE_CHECKING:
    from gpiozero import Button
else:
    Button = typing.Any

try:
    from gpiozero import Button
except ImportError:
    from gpio_mock import Button


def setup_zero_cross_detection(pin):
    logging.info("Setting up zero-cross detection")
    zero_cross = Button(pin, pull_up=False)
    zero_cross.when_pressed = zero_cross_callback
    return zero_cross

def zero_cross_callback():
    logging.debug("Zero-cross detected")
    # This function will be called when a zero-cross is detected
    pass
