import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
#ser.flush()
#s = ("Hello Arduino".encode())

#print(s)

ser.write("Hello Arduino".encode())
#ser.open()


#time.sleep(1)
numberofbytes = ser.inWaiting()
line = ser.read(numberofbytes)
time.sleep(2)
print(numberofbytes)
#print("Sent: "+ s.decode())
print("Recieved: " + line.decode())
    

