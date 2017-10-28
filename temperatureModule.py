import time

def getTemperatureFormatted():
	f = open("/sys/bus/w1/devices/28-0316a1017dff/w1_slave",'r')
	f.readline()
	temp = int(f.readline().split(" ")[9].replace("t=",""))
	tempPrec = "%.1f"%(temp/1000)
	return tempPrec
    
def getTemperature():
	f = open("/sys/bus/w1/devices/28-0316a1017dff/w1_slave",'r')
	f.readline()
	temp = int(f.readline().split(" ")[9].replace("t=",""))
	return temp
