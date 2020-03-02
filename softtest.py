import serial
import time
import sys
import select

from random import randint

ser=serial.Serial('/dev/ttyUSB2',115200)


while True:
    s = randint(0,10)
    ser.write(s)
    print(s)
    time.sleep(1) 

    #numberofbytes = ser.inWaiting()

    #line = ser.read(numberofbytes)      
    #print("Recieved: " + line.decode())

    
