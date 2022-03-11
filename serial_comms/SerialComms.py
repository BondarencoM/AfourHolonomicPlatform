# imports
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
    #ser = serial.Serial('COM6', 9600, timeout=1)
    #ser.reset_input_buffer()

    testOnce = 1

    while True:
        if testOnce == 1:
            ser.write(b"\x01")  # move command
            ser.write(b"\x40")  # 90 degrees angle
            ser.write(b"\x73")  # 45% speed
            ser.write(b"\x03")  # 1000cm distance
            ser.write(b"\xE8")  # 1000cm distance
            # change test
            testOnce = 2

        time.sleep(2)

        if testOnce == 2:
            ser.write(b"\x02")  # rotate command
            ser.write(b"\x80")  # 180 degrees angle
            ser.write(b"\x5C")  # 36% speed
            ser.write(b"\x00")  # unwanted distance
            ser.write(b"\x39")  # 57cm distance
            # change test
            testOnce = 0

        line = ser.readline()
        print(line)
        
        

        time.sleep(1)
    