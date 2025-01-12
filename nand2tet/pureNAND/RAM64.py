from RAM8 import RAM8
from Gates import Mux8, Dmux8


class RAM64():
    def __init__(self):
        self.size = 8
        self.reg64 = [RAM8() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal8 = Dmux8(load, address[0:3])
        for position8, load8 in enumerate(signal8):
            self.reg64[position8].update(word, load8, address[3:6], clock) 

    def state(self, address):
        output = []
        for i in range(16):
            signal = [self.reg64[reg].state(address[3:6])[i] for reg in range(self.size)]
            output.append(Mux8(signal, address))
        return output


# ----------------------------------------------------------------------
def test():
    ram = RAM64()
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
                    out = ram.reg64[i].reg8[j].state()
                    temp = [i, j]
                    addr = ''.join(bin(x)[2:].zfill(3) for x in temp)
                    print(f'{count} {addr} {out}')
                    count += 1
        tick = 1 - tick

if __name__ == '__main__':
    test()
            




