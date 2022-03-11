COMMANDS = {
    'Precision Move': 1,
    'Arbitrary Move': 2,
    'Spin': 3,
}

def ArbitraryMove(angle: int, speed: int, distance: int):
    return bytearray([
        COMMANDS['Arbitrary Move'],
        angle,
        speed,
    ]) + distance.to_bytes(2, 'big', signed=False)