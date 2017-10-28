import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin = -1

def initialize(xpin):
	pin = xpin
	GPIO.setup(pin, GPIO.IN)
	
def getValue():
	i = GPIO.input(xpin)
