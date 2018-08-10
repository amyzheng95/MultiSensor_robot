import RPi.GPIO as GPIO
import time
import sensor

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(3,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(20,GPIO.OUT)
	GPIO.setup(27,GPIO.OUT)
	GPIO.setup(21,GPIO.OUT)
	#p1 = GPIO.PWM(3,50)
	#p2 = GPIO.PWM(27,50)

def forward(tf):
	init()
	#Set the pins for the duty cycles
	p1 = GPIO.PWM(20,50)
        p2 = GPIO.PWM(16,50)
	#Start of duty cycle 25% (0-100)
	p1.start(30)
	p2.start(30)
	#right forward
	GPIO.output(20, True)
        GPIO.output(27, True)
        GPIO.output(21, False)
	#left forward
	GPIO.output(13, False)
	GPIO.output(3, True)
	GPIO.output(16, True)

	time.sleep(tf)
	GPIO.cleanup()

def backward(tf):
	init()
	#Set the pins for the duty cycles
	p1 = GPIO.PWM(21,50)
        p2 = GPIO.PWM(13,50)
	#Start of duty cycle 25% (0-100)
	p1.start(30)
	p2.start(30)
	#right backward
	GPIO.output(20, False)
        GPIO.output(27, True)
        GPIO.output(21, True)
	#left backward
	GPIO.output(13, True)
	GPIO.output(3, True)
	GPIO.output(16, False)

	time.sleep(tf)
	GPIO.cleanup()

def turnRight(tf):
	init()
	p1 = GPIO.PWM(21,25)
	p2 = GPIO.PWM(16,25)
	p1.start(50)
	p2.start(30)
	#right backward
        GPIO.output(20, False)
        GPIO.output(27, True)
        GPIO.output(21, True)
	#left forward
	GPIO.output(13, False)
        GPIO.output(3, True)
        GPIO.output(16, True)
	time.sleep(tf)
	GPIO.cleanup()
	
def turnLeft(tf):
	init()
	p1 = GPIO.PWM(13,25)
	p2 = GPIO.PWM(20,10)
	p1.start(30)
	p2.start(50)
	#right forward
        GPIO.output(20, True)
        GPIO.output(27, True)
        GPIO.output(21, False)
	#left backward
	GPIO.output(13, True)
        GPIO.output(3, True)
        GPIO.output(16, False)
	time.sleep(tf)
	GPIO.cleanup()
        
def stopMotor(tf):
	init()
	GPIO.output(20, False)
        GPIO.output(27, False)
        GPIO.output(21, False)
	GPIO.output(13, False)
	GPIO.output(3, False)
	GPIO.output(16, False)

	time.sleep(tf)
	GPIO.cleanup()

#20 True,21 False right forward

#21 True,20 False right backward

#16 False,13 True left backward

#16 True, 13 False left forward

