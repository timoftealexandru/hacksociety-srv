import subprocess;

def takePicture(resX, resY, name, path):
	res = subprocess.Popen(["fswebcam", "-r " + str(resX) + "x" + str(resY), name], shell=False, stdout=subprocess.PIPE, cwd=path);
	output = res.communicate()[0];
	
takePicture(640, 480, "test.jpg", "/home/pi/Desktop")
