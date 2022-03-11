from arfourWeb.machineControl.Protocol import ArbitraryMove
import serial
import time
# serCom = serial.Serial("/dev/ttyS0", 9600)
serCom = type('obj', (object,), {'write' : lambda x: 1})


class MachineControl:
    presetMoves = {}

    def arbitraryMove(self, angle, speed):
        val = ArbitraryMove(
            angle=mapToByte(angle, 0, 359),
            speed=mapToByte(speed, 0, 100),
            distance=5,
        )
        print([x for x in val])
        serCom.write(val)
        time.sleep(1)
        print(serCom.readline())

    def presetMove(self, id):
        if id == 1 :
            val = ArbitraryMove(
                angle=mapToByte(0, 0, 359),
                speed=mapToByte(35, 0, 100),
                distance=465,
            )
            print([x for x in val])
            serCom.write(val)
            time.sleep()
            print(serCom.readline())


def mapToByte(value, rangeStart, rangeEnd):
    return round(255 / (rangeEnd - rangeStart) * (value - rangeStart))
