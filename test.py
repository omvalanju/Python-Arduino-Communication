import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)

var = ('Hello'.encode())

#print(var)

ser.write(var)

time.sleep(1)
numberofbytes = ser.inWaiting()
line = ser.read(numberofbytes)
print("Output: " + line.decode())

