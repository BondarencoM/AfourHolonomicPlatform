from yaml import serialize
from arfourWeb.machineControl.Protocol import ArbitraryMove, OneMeterMove, StopCommand, TenMeterMove
import serial
import time
serCom = serial.Serial("COM11", 9600)
# serCom = type('obj', (object,), {'write' : lambda x: 1, 'readline': lambda x: 1})

def mapToByte(value, rangeStart, rangeEnd):
    return round(255 / (rangeEnd - rangeStart) * (value - rangeStart))


def SquareMove(direction):
    return OneMeterMove(
                angle=mapToByte(direction, 0, 359),
                speed=mapToByte(50, 0, 100),
                distance=0,
            )


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

    def presetMove(self, id):
        if id == 1:
            val = TenMeterMove(
                angle=mapToByte(0, 0, 359),
                speed=mapToByte(50, 0, 100),
                distance=0,
            )
            print([x for x in val])
            serCom.write(val)
        elif id == 2:
            serCom.write(SquareMove(0))
            time.sleep(2)

            serCom.write(SquareMove(90))
            time.sleep(2)

            serCom.write(SquareMove(180))
            time.sleep(2)

            serCom.write(SquareMove(270))
            time.sleep(2)
    
    def stop(self):
        serCom.write(StopCommand())