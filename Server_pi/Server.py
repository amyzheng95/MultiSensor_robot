#!/usr/bin/env python
import socket
import sys
import motor
import RPi.GPIO as GPIO
import sensor

#local host name
host = 'raspberrypi.local'
#any port above 1024
port = 4242 

def choice(input,conn):
    t=5
    start = t
    inc = 0.5
    try:
	if input == 'f':
            while t>0:
                if(sensor.willFrontCrash()):
                    print('stopped after ' + str(start-t))
                    break
                motor.forward(inc)
                t = t-inc
	    print('Move forward')
    	elif input == 'b':
            while t>0:
                if(sensor.willBackCrash()):
                    print('stopped after ' + str(start-t))
                    break
                motor.backward(inc)
                t = t-inc
	    print('Move backward')
    	elif input == 'r':
            motor.turnRight(t)
	    print('turn right')
    	elif input == 'l':	
            motor.turnLeft(t)
	    print('turn left')
	elif input == 's':
            reading = sensor.getAllSensor()
            print('Read all sensors')
            print(reading)
            result = " ".join(reading)
            conn.send(result)
    except KeyboardInterrupt:
	    print('key board interrupted!')
    finally:
            print('done')
    conn.send("\n")

def menu(conn):
    conn.send ('Welcome to the MultiSensor Robot server\n')
    conn.send ('s - get sensor readings\n')
    conn.send ('f -go straight\n')
    conn.send ('b - go backwards\n')
    conn.send ('l - go left\n')
    conn.send ('r - go right\n')
    conn.send ('p - take a pic\n')
    conn.send ('q - quit\n\n')     

def getClientInput(conn):
    try:
        conn.send('Server:\n')
        data,addr = conn.recv(1024) 
        if data is not None and len(str(data))!=0 :
            input = str(data)
            return input
        return ''
    except socket.error,e:
        print "Error receiving data: %s" %e
        sys.exit(1)
    except ValueError:
        print "this is not a valid input"
        sys.exit(1)
        
def close_connection(conn):
    conn.close()

def server(conn):
    menu(conn) #displays the menu
    while True:
        input = getClientInput(conn)
        if(input == 'q'):
            close_connection(conn)
            print("Closed connection with Client on port " + str(port) )
            break
	elif(input == ''):
            conn.send("Server: Please enter a valid input\n")
        else:
            choice(input,conn)

def startServer():
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # instance created
        try:
            s.bind((host, port)) # bind host and port
            print("Connected")
            s.listen(1)#number of clients the server can listen to
            print("Listening on port " + str(port))
        except socket.error as msg:
            print'Bind failed.' + str(msg[0]) + ' Message: ' + msg[1] +'Please choose another port'
            sys.exit()
            
        while True:
            conn, addr = s.accept() # Accept connection from client
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            server(conn)
try:      
    startServer()
except KeyboardInterrupt:
    print("\nKeyboard Interruption, end program")
    sys.exit(1)

            
