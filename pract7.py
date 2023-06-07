def main(x):
    x = int(x, 16)
    maskP1 = 0b00000000000000000011111
    maskP2 = 0b00000000000001111100000
    maskP3 = 0b00000011111110000000000
    maskP4 = 0b00011100000000000000000
    maskP5 = 0b11100000000000000000000
    P1 = x & maskP1
    P2 = (x & maskP2) >> 5
    P3 = (x & maskP3) >> 10
    P4 = (x & maskP4) >> 17
    P5 = (x & maskP5) >> 20
    res = {}
    res['P1'] = str(int(P1))
    res['P2'] = str(int(P2))
    res['P3'] = str(int(P3))
    res['P4'] = str(int(P4))
    res['P5'] = str(int(P5))
    return res


print(main('0x6facdf'))
print(main('0x40a076'))
print(main('0x4dc3ed'))
print(main('0x4624d5'))