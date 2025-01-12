from Dclass import Dlatch
from Not import Not


class DFF():
    def __init__(self):
        self.master = Dlatch()
        self.slave = Dlatch()
        self.mid = 0
        self.clock = 0

    def update(self, d):
        if self.clock == 0:
            self.master.update(d, Not(self.clock))
            self.mid = self.master.state()[0]
        else: 
            self.slave.update(self.mid, self.clock)
        self.clock = 1 - self.clock 

    def state(self):
        return self.slave.state()

    def resetClock(self, c):
        self.clock = c


def test():
    latch = DFF()
    while True:
        if latch.clock == 0:
            d = input()
            latch.update(d)
        else:
            d = latch.mid        
            print(f'State: {latch.state()}')
            latch.update(d)

if __name__ == "__main__":
    test()

