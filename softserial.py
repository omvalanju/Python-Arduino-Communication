import serial
import time
import sys
import select
from threading import Thread

ser=serial.Serial('/dev/ttyACM0',19200)
ser.write("Python Initiated".encode())
def send():
    while True:
        s=input("Enter Message: ")
        print ("\033[A                                             \033[A")

        if (len(s) != 0):
            ser.write(s.encode())
            print("Transmitted: " +s)
         
        else:
            None
            #print("else satisfied")
            #print ("\033[A                             \033[A")

def recieve():
    while True:
        numberofbytes = ser.inWaiting()
        #print(numberofbytes)
        #time.sleep(1)
        if (numberofbytes == 0):
            None
        else:
            line = ser.read(numberofbytes)
            #sendthread.kill()
            #print ("\033[A                             \033[A")
            print("Recieved: " + line.decode())
            #print ("\033[A                             \033[A")
            #sendthread.start()


sendthread = Thread(target = send)
sendthread.start()

recievethread = Thread(target = recieve)
recievethread.start()

