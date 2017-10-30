import RPi.GPIO as GPIO
import time

class buzz():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        
    def start(self):
        GPIO.output(7, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(7, GPIO.LOW)