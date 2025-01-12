from Gates import Mux
from DFF import DFF


class Bit():
    def __init__(self):
        self.dff = DFF()

    def update(self, in1, load, clock):
        in2 = self.dff.slave.state() 
        mux = Mux([in2, in1], load) 
        self.dff.update(mux, clock) 

    def state(self):
        return self.dff.state()


# ----------------------------------------------------------------------
def test():
    bit = Bit()
    tick = 0
    while True:
        if tick == 0:
            d = int(input('Input: '))
            load = int(input('Load?: '))
        else:
            d = bit.dff.master.state()
            print(bit.state())
        bit.update(d, load, tick)
        tick = 1 - tick

if __name__ == '__main__':
    test()
