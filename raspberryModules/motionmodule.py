import RPi.GPIO as GPIO
import time

class motion():
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.pin = 11
        GPIO.setup(self.pin, GPIO.IN)
	
    def getValue(self):
        i = GPIO.input(self.pin)
        time.sleep(0.2)
        return i
