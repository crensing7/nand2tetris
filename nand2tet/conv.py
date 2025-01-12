def b2d(line):
    d = 0 
    for power, bit in enumerate(reversed(line)):
        d += bit * (2 ** power) 
    return d      

def d2b(line):
    b = []
    temp = bin(int(line))[2:]
    b += ['0' for i in range(16 - len(temp))]
    for bit in temp:
        b += [bit]
    return b
