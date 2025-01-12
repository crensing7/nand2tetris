from RAM64 import RAM64
from Gates import Mux8, Dmux8


class RAM512():
    def __init__(self):
        self.size = 8
        self.reg512 = [RAM64() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal64 = Dmux8(load, address[0:3])
        for position64, load64 in enumerate(signal64):
            self.reg512[position64].update(word, load64, address[3:9], clock) 

    def state(self, address):
        output = []
        for i in range(16):
            signal = [self.reg512[reg].state(address[3:9])[i] for reg in range(self.size)]
            output.append(Mux8(signal, address))
        return output


# ----------------------------------------------------------------------
def test():
    ram = RAM512()
    tick = 0
    while True:
        choice = input('Read/Write/All?: ')
        if choice == 'r':
            address = [int(_) for _ in input('Address: ')]
            print(ram.state(address))
        if choice == 'w':
            word = [int(_) for _ in input('Word: ')]
            address = [int(_) for _ in input('Address: ')]
            ram.update(word, 1, address, 0)
            ram.update(word, 1, address, 1)
        if choice == 'a':
            count = 0
            for i in range(ram.size):
                for j in range(ram.size):
                    for k in range(ram.size):
                        out = ram.reg512[i].reg64[j].reg8[k].state()
                        temp = [i, j, k]
                        addr = ''.join(bin(x)[2:].zfill(3) for x in temp)
                        print(f'{count} {addr} {out}')
                        count += 1
        tick = 1 - tick

if __name__ == '__main__':
    test()
            




