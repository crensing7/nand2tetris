from RAM4K import RAM4K
from Gates import Mux4, Dmux4


class RAM16K():
    def __init__(self):
        self.size = 4
        self.width = 16
        self.reg16K = [RAM4K() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal4K = Dmux4(load, address[0:2])
        for position4K, load4K in enumerate(signal4K):
            self.reg16K[position4K].update(word, load4K, address[2:14], clock) 

    def state(self, address):
        output = []
        for i in range(self.width):
            signal = [self.reg16K[reg].state(address[2:14])[i] for reg in range(self.size)]
            output.append(Mux4(signal, address))
        return output


def test():
    ram = RAM16K()
    for i in range(ram.size):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    out = ram.reg16K[i].reg4K[j].reg512[k].reg64[l].full()
                    temp = [i, j, k, l]
                    addr = ''.join(bin(x)[2:].zfill(3) for x in temp)[1:]
                    print(f'{addr} {out}')

if __name__ == '__main__':
    test()
            




