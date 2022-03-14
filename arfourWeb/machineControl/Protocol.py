COMMANDS = {
    'Stop': 0,
    'Move': 1,
    'Rotate': 2,
    'TenMeterMove': 3,
    'OneMeterMove': 4,
}

def ArbitraryMove(angle: int, speed: int, distance: int):
    return bytearray([
        COMMANDS['Arbitrary Move'],
        angle,
        speed,
    ]) + distance.to_bytes(2, 'big', signed=False)

def OneMeterMove(angle: int, speed: int, distance: int):
    return bytearray([
        COMMANDS['OneMeterMove'],
        angle,
        speed,
    ]) + distance.to_bytes(2, 'big', signed=False)

def TenMeterMove(angle: int, speed: int, distance: int):
    return bytearray([
        COMMANDS['TenMeterMove'],
        angle,
        speed,
    ]) + distance.to_bytes(2, 'big', signed=False)

def StopCommand():
    return bytearray([0] * 5)