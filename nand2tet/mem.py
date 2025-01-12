import sys
from conv import b2d


class rom:
    def __init__(self, size):
        self.size = size
        self.selected = 0
        self.array = [[0 for _ in range(16)] for i in range(size)]
    
    def load(self):
        with open(f'{sys.argv[1]}') as f:
            code = [[int(i) for i in line.strip()[:16]] for line in f.readlines()]
        for instruction in code:
            self.update(instruction)
            self.next()
        self.addr(0)
    
    def state(self):
        return self.array[self.selected]

    def update(self, word):
        self.array[self.selected] = word

    def addr(self, address):
        self.selected = address

    def next(self):
        self.selected += 1 

    def full(self):
        for index, register in enumerate(self.array[:150]):
            print(f'{index:02d}: {register}')


class ram:
    def __init__(self, size):
        self.size = size
        self.selected = 0
        self.array = [[0 for _ in range(16)] for i in range(size)]
        self.cache = [['0' * 16 for _ in range(32)] for i in range(256)] 

    def state(self):
        return self.array[self.selected]

    def update(self, word):
        self.array[self.selected] = word
        if 16384 <= self.selected < 24577:
            offset = self.selected - 16384 
            row = offset // 32
            start = 16384 + (row * 32)
            data = [''.join('1' if bit else '0' for bit in line) for line in self.array[start:start + 32]]
            self.cache[row] = data 

    def addr(self, address):
        self.selected = address

    def next(self):
        self.selected += 1 
        
    def full(self):
        for register in self.array[:30]:
            print(register)


if __name__ == '__main__':
    mem = rom(32768)
    mem.load()
    mem.full()
    print



