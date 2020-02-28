import serial
import time

ser=serial.Serial('/dev/ttyACM1',9600)

s = "Hello Arduino"
ser.write(s.encode())


print("Sent: " + s)

time.sleep(2)
numberofbytes = ser.inWaiting()
line = ser.read(numberofbytes)

print("Recieved: " + line.decode())

time.sleep(2)
numberofbytes = ser.inWaiting()
line = ser.read(numberofbytes)

print("Rx: " + line.decode())

time.sleep(2)
s = input("Enter Message:")
ser.write(s.encode())

time.sleep(7)
numberofbytes = ser.inWaiting()
line = ser.read(numberofbytes)
print("Recieved from arduino: " + line.decode())
