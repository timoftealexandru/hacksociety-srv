import time

class temperature():
    def __init__(self):
        self.path = "/sys/bus/w1/devices/28-0316a1017dff/w1_slave"
        
    def getTemperatureFormatted(self):
        f = open(self.path,'r')
        f.readline()
        temp = int(f.readline().split(" ")[9].replace("t=",""))
        tempPrec = "%.0f"%(temp/1000)
        return tempPrec
    
    def getTemperature(self):
        f = open(self.path,'r')
        f.readline()
        temp = int(f.readline().split(" ")[9].replace("t=",""))
        return temp
