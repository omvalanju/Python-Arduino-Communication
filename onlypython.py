import serial
import time



def recieve():
    while True:
        numberofbytes = ser.inWaiting()
        #print(numberofbytes)
        #time.sleep(1)
        if (numberofbytes == 0):
            None
        else:
            line = ser.read(numberofbytes)
            print("Recieved: " + line.decode())

def send():
    


