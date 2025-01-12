from Gates import Not
from Dlatch import Dlatch


class DFF():
    def __init__(self):
        self.master = Dlatch()
        self.slave = Dlatch()

    def update(self, d, clock):
        self.master.update(d, Not(clock))
        mid = self.master.state()
        self.slave.update(mid, clock)

    def state(self):
        return self.slave.state()

def test():
    dff = DFF()
    tick = 0
    while True:
        if tick == 0:
            d = int(input('Input: '))
            print(dff.state())
        else:
            d = dff.master.state()
        dff.update(d, tick)
        
        tick = 1 - tick 

if __name__ == '__main__':
    test()
