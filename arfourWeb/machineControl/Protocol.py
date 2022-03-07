COMMANDS = {
    'Precision Move': 1,
    'Arbitrary Move': 2,
    'Spin': 3,
}


def ArbitraryMove(angle: int, speed: int):
    return bytearray([
        COMMANDS['Arbitrary Move'],
        angle,
        speed,
    ])
