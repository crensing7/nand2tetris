from DFF import DFF
from Mux import Mux


class Bit():
    def __init__(self):
        self.dff = DFF()
        self.mux = 0 

    def update(self, in1, load):
        in2 = self.dff.slave.state()[0] 
        self.mux = Mux(in2, in1, load) 
        self.dff.update(self.mux) 

    def state(self):
        return self.dff.state()[0]


def test():
    bit = Bit()
    while True:
        if reg.dff.clock == 0:
            d = input('Input: ')
            load = input('Load?: ')
            reg.update(d, load)
        else:
            d = reg.dff.mid
            print(reg.state())
            reg.update(d, load)

if __name__ == '__main__':
    test()    

