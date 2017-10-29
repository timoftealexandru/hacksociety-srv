import RPi.GPIO as GPIO2
import time

class tilt():
    def __init__(self):
        GPIO2.setmode(GPIO2.BOARD)
        GPIO2.setup(37, GPIO2.IN)

    def getValue(self):
        return GPIO2.input(37)