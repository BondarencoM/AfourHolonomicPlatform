from arfourWeb.machineControl.Protocol import ArbitraryMove
import serial

# serCom = serial.Serial("/dev/ttyS0", 9600)


class MachineControl:
    presetMoves = {}

    def arbitraryMove(self, angle, speed):
        val = ArbitraryMove(
            angle=mapToByte(angle, 0, 359),
            speed=mapToByte(speed, 0, 100),
        )
        print([x for x in val])
        # serCom.write(val)


def mapToByte(value, rangeStart, rangeEnd):
    return round(255 / (rangeEnd - rangeStart) * (value - rangeStart))
