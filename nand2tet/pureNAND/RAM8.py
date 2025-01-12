from Register import Register
from Gates import Mux8, Dmux8
from Counter import Counter


class RAM8():
    def __init__(self):
        self.size = 8
        self.width = 16
        self.reg8 = [Register() for _ in range(self.size)]

    def update(self, word, load, address, clock):
        signal = Dmux8(load, address)
        for position, load in enumerate(signal): 
            self.reg8[position].update(word, load, clock)

    def state(self, address):
        output = []
        for i in range(self.width):
            signal = [self.reg8[reg].state()[i] for reg in range(self.size)]
            output.append(Mux8(signal, address))
        return output 
    
    def full(self):
        line = []
        for i in range(self.size):
            line.append(self.reg8[i].state())
        return line


    def load(self, program):
        address = Counter()
        binary = []
        with open(program) as f:
            for line in f:
                code = [int(_) for _ in line.strip()]
                self.update(code, 1, address.state()[-3:], 0)    
                self.update(code, 1, address.state()[-3:], 1)    
                address.inc(0)
                address.inc(1)



        


        
                



# ----------------------------------------------------------------------
def test():
    ram = RAM8()
    tick = 0
    while True:
        choice = input('Read/Write/All? ')
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
                out = ram.reg8[i].state()
                temp = [i]
                addr = ''.join(bin(x)[2:].zfill(3) for x in temp)
                print(f'{count} {addr} {out}')
                count += 1
        tick = 1 - tick

if __name__ == '__main__':
    ram = RAM8()
    counter = Counter()
    program = './program.txt'
    ram.load(program)
    print(ram.full())
