import time  
import RPi.GPIO as GPIO

class rgbModule():
    def __init__(self):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BOARD)
        self.red = 29
        self.green = 31
        self.blue = 33

        GPIO.setup(self.red, GPIO.OUT) #setup all the pins  
        GPIO.setup(self.green, GPIO.OUT)  
        GPIO.setup(self.blue, GPIO.OUT)

        self.Freq = 100 #Hz  

        self.RED = GPIO.PWM(self.red, self.Freq)
        self.GREEN = GPIO.PWM(self.green, self.Freq)
        self.BLUE = GPIO.PWM(self.blue, self.Freq)

        self.RED.start(0)
        self.GREEN.start(0)
        self.BLUE.start(0)
        self.leds={'b':self.RED, 'r':self.GREEN, 'g':self.BLUE}

    def turnOnLed(self,led):
        self.leds[led].start(0)
        self.leds[led].ChangeDutyCycle(100)
        time.sleep(5)
        
    def turnOffLed(self,led):
        self.leds[led].stop()

