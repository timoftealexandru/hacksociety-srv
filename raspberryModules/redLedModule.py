import RPi.GPIO as GPIO
import time

LedPin = -1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

def Initialize(xpin):
	LedPin = xpin
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	
def startRedLed():
	GPIO.output(LedPin, GPIO.HIGH)
	
def stopRedLed():
	GPIO.output(LedPin, GPIO.LOW)
