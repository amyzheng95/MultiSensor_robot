#!/usr/bin/env python
import socket
import sys
import motor
import RPi.GPIO as GPIO
import sensor

host = 'raspberrypi.local'
port = 4242 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.bind((host, port))
except socket.error as msg:
	print'Bind failed. Error Code: ' + str(msg[0]) + 'Message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Listening and waiting for command' 
while True:
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	conn.send ('Welcome to the MultiSensor Robot server\ns - get sensor readings\nf - go straight\nb - go backwards\nl - go left\nr - go right\np - take a pic\nq - quit\n\n')
	
	while True:
		data,addr = conn.recv(1024)
		if data is not None and len(str(data))!=0 :
                        if input == 'q':
                            conn.shutdown(socket.SHUT_RDWR)
                            conn.close()
                            break
			input = str(data)
			t = 5
		
			try:
				if input == 'f':
					motor.forward(t)
					print('Move forward')
    				elif input == 'b':
                                        motor.backward(t)
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
                                        conn.send(" ".join(reading))
			
			except KeyboardInterrupt:
				print('key board interrupted!')

			finally:
                                print('done')
	
			print(str(data))
			n ="\n"
			conn.send(n)
		else:
			break
	#conn.close()
