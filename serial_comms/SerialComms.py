
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    testOnce = 1

    while True:
        if testOnce == 1:
            ser.write(b"cest")
            testOnce = 0


        line = ser.readline()
        print(line)

        time.sleep(1)
    