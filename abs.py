import serial
ser = serial.Serial('/dev/ttyACM1',9600,timeout=1)

try:
 while 1:
  ser.write('s',);  
  print(ser.readall());
except:
 ser.close();
