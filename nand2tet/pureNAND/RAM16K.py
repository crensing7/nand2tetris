from RAM4K import RAM4K
from Gates import Mux4, Dmux4


class RAM16K():
    def __init__(self):
        self.size = 4
        self.reg16K = [RAM4K() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal4K = Dmux4(load, address[0:2])
        for position4K, load4K in enumerate(signal4K):
            self.reg16K[position4K].update(word, load4K, address[2:14], clock) 

    def state(self, address):
        output = []
        for i in range(16):
            signal = [self.reg16K[reg].state(address[2:14])[i] for reg in range(self.size)]
            output.append(Mux4(signal, address))
        return output


# ----------------------------------------------------------------------
def test():
    ram = RAM16K()
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
                for j in range(8):
                    for k in range(8):
                        for l in range(8):
                            for n in range(8):
                                out = ram.reg16K[i].reg4K[j].reg512[k].reg64[l].reg8[n].state()
                                temp = [i, j, k, l, n]
                                addr = ''.join(bin(x)[2:].zfill(3) for x in temp)
                                print(f'{count} {addr} {out}')
                                count += 1
        tick = 1 - tick

if __name__ == '__main__':
    test()
            




