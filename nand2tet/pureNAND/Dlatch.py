from Gates import Nand, Not


class Dlatch():
    def __init__(self):
        self.q = 0
        self.p = 1

    def update(self, d, clock):
        s = Nand(d, clock) 
        r = Nand(Not(d), clock) 

        midq = Nand(s, self.p)
        midp = Nand(r, self.q)

        self.q = Nand(s, midp)
        self.p = Nand(r, midq)

    def state(self):
        return self.q 

def test():
    latch = Dlatch()
    while True:
        d = int(input('Data: '))
        clock = int(input('Clock: '))
        latch.update(d, clock)
        print(latch.state())

if __name__ == '__main__':
    test()

