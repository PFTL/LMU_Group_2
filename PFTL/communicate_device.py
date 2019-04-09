import serial
import time


dev = serial.Serial('/dev/ttyACM0')
time.sleep(1)

dev.write(b'IDN\n')
answer = dev.readline()

print(answer)

dev.write(b'OUT:CH0:4000\n')
time.sleep(0.05)
dev.write(b'IN:CH0\n')
voltage = dev.readline()
print('The output is {} and the input is {}'.format(4000, voltage))

# for i in range(10):
#     dev.write(b'OUT:CH0:0\n')
#     time.sleep(.5)
#     dev.write(b'OUT:CH0:4000\n')
#     time.sleep(.5)