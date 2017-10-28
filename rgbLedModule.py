import time  
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

red = -1
green = -1
blue = -1

RED = 0
GREEN = 0
BLUE = 0
leds = {'r' : RED, 'g' : GREEN, 'b' : BLUE}

def Initialize(r,g,b):
	#set the pins of red, green and blue
	red = r
	green = g
	blue = b
	
	GPIO.setup(red, GPIO.OUT) #setup all the pins  
	GPIO.setup(green, GPIO.OUT)  
	GPIO.setup(blue, GPIO.OUT)

	Freq = 100 #Hz  

	RED = GPIO.PWM(red, Freq)
	GREEN = GPIO.PWM(green, Freq)
	BLUE = GPIO.PWM(blue, Freq)

def startLed(led):
	leds[led].start()
	leds[led].ChangeDutyCycle(100)
	
def stopLed(led):
	leds[led].stop()

