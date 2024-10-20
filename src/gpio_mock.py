class Button:
    def __init__(self, pin, pull_up=True):
        pass
    def when_pressed(self, callback):
        pass

class OutputDevice:
    def __init__(self, pin):
        pass
    def on(self):
        pass
    def off(self):
        pass

class PWMOutputDevice:
    def __init__(self, pin, frequency=100):
        pass
    @property
    def value(self):
        return 0
    @value.setter
    def value(self, val):
        pass