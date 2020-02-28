import serial
import time
import sys
import select

ser=serial.Serial('/dev/ttyACM2',19200)
flag = 0

while True:
    print("Enter Message: ")
    i, o, e = select.select( [sys.stdin], [], [], 5 )

    if (i):
        #s = input("Enter Message: ")
        #s = "Hello Arduino"
        s = sys.stdin.readline().strip()
        ser.write(s.encode())
        print("Transmitted: " + s)
        flag = 0
    else:
        #print ("Nothing to Transmit")
        None
        flag = 1

    if (flag == 1):
        None
    
    #time.sleep(2)
 
    numberofbytes = ser.inWaiting()

    #if (numberofbytes == 0):
        #None
    #else:
    line = ser.read(numberofbytes)      
    print("Recieved: " + line.decode())

    #time.sleep(2)

    #line = ser.read(numberofbytes)
       

    #print("Recieved: " + line.decode())
    #serial.flush()
