import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BOARD)
    
def getAllSensor():
    a = getSensor(12,11)
    b = getSensor(3,7)
    c = getSensor(31,29)
    d = getSensor(37,35)
    e = getSensor(21,22)
    f = getSensor(23,24)
    ans = [a,b,c,d,e,f]
    ans = [str(i) for i in ans]
    return ans
    
def willFrontCrash():
    a = getSensor(12,11)
    b = getSensor(3,7)
    c = getSensor(31,29)
    if(a<20 or b<20 or c<20):
        print("Front might crash")
        return True
    return False

def willBackCrash():
    d = getSensor(37,35)
    e = getSensor(21,22)
    f = getSensor(23,24)
    if(d<20 or e<20 or f<20):
        print("Back might crash")
        return True
    return False
    
def getSensor(TRIG,ECHO):
	try:
		init()
    		#Set the pins for TRIG, trig is the output pin 
    		GPIO.setup(TRIG,GPIO.OUT)
    		#Set the pins for ECHO, echo is the input pin
    		GPIO.setup(ECHO,GPIO.IN)
    		#3.3v sent to trig
    		GPIO.output(TRIG,1)
    		#turn off the trig pin
    		GPIO.output(TRIG,0)
       		while GPIO.input(ECHO) == 0:
          		pass
       		start = time.time()

       		while GPIO.input(ECHO) == 1:
        		pass
       		stop = time.time()
       		reading = (stop - start) * 17000
                return reading
            
   	except KeyboardInterrupt:
      		print "Interrupted by keyboard"
   	except:
      		print "Other error or exception occured"
   	finally:
		GPIO.cleanup()

    
    
