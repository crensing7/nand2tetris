from RAM4K import RAM4K
from Gates import Mux8, Dmux8
from Counter import Counter

class ROM32K():
    def __init__(self):
        self.size = 8
        self.reg32K = [RAM4K() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal4K = Dmux8(load, address[0:3])
        for position4K, load4K in enumerate(signal4K):
            self.reg32K[position4K].update(word, load4K, address[3:15], clock) 

    def state(self, address):
        output = []
        for i in range(16):
            signal = [self.reg32K[reg].state(address[3:15])[i] for reg in range(self.size)]
            output.append(Mux8(signal, address))
        return output

    def load(self, program):
        binary = []
        with open(program) as f:
           data = f.readlines()
        for line in data:
            binary += [[int(_) for _ in line.strip()]]
        return binary
        






# ----------------------------------------------------------------------
def test():
    ram = ROM32K()
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
                            for m in range(ram.size):
                                out = ram.reg32K[i].reg4K[j].reg512[k].reg64[l].reg8[m].state()
                                temp = [i, j, k, l, m]
                                addr = ''.join(bin(x)[2:].zfill(3) for x in temp)[1:]
                                print(f'{count} {addr} {out}')
                                count += 1
        tick = 1 - tick


if __name__ == '__main__':
    test()
##    rom = ROM32K()
##    address = [int(_) for _ in input('Address: ')]
##    program = './program.txt'
##    code = rom.load(program)
##    print(code)
##    print()
##    print(address)
##    rom.update(code[0], 1, address, 0)
##    rom.update(code[0], 1, address, 1)
##    print(rom.state(address))

    
   



