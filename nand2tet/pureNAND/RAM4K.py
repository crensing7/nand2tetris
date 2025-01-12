from RAM512 import RAM512
from Gates import Mux8, Dmux8


class RAM4K():
    def __init__(self):
        self.size = 8
        self.reg4K = [RAM512() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal512 = Dmux8(load, address[0:3])
        for position512, load512 in enumerate(signal512):
            self.reg4K[position512].update(word, load512, address[3:12], clock) 

    def state(self, address):
        output = []
        for i in range(16):
            signal = [self.reg4K[reg].state(address[3:12])[i] for reg in range(self.size)]
            output.append(Mux8(signal, address))
        return output


# ----------------------------------------------------------------------
def test():
    ram = RAM4K()
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
                        for l in range(ram.size):
                            out = ram.reg4K[i].reg512[j].reg64[k].reg8[l].state()
                            temp = [i, j, k, l]
                            addr = ''.join(bin(x)[2:].zfill(3) for x in temp)
                            print(f'{count} {addr} {out}')
                            count += 1
                print()
        tick = 1 - tick

if __name__ == '__main__':
    test()
            




