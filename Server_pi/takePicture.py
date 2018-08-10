# import the necessary packages
from picamera import PiCamera
from time import sleep

#def takephoto():
camera = PiCamera()
sleep(5)
camera.capture('/home/pi/Desktop/testComponentFile/image.jpg')

#takephoto()