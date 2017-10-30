import subprocess;

class cameramodule():
    def __init__(self):
        self.resX = 640
        self.resY = 480
        self.name = "img.jpg"
        self.path = "/home/pi/hacksociety-srv"

    def takePicture(self):
        res = subprocess.Popen(["fswebcam", "-r " + str(self.resX) + "x" + str(self.resY), self.name], shell=False, stdout=subprocess.PIPE, cwd=self.path);
        output = res.communicate()[0];
        return self.name
	
#takePicture(640, 480, "img.jpg", "/home/pi/hacksociety-srv")
#foo = cameraModule()
#foo.takePicture()
