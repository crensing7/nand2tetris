from Bit import Bit


class Register():
    def __init__(self):
        self.size = 16
        self.bits = [Bit() for _ in range(self.size)]

    def update(self, word, load, clock):
        if len(word) != self.size:
            raise ValueError(f'Input must be {self.size} bit word!')
        for i in range(self.size):
            self.bits[i].update(word[i], load, clock)

    def state(self):
        return [self.bits[i].state() for i in range(self.size)]


# ----------------------------------------------------------------------  
def test():
    reg = Register()
    tick = 0
    while True:
        if tick == 0:
            word = [int(_) for _ in input('Word: ')]  
            load = int(input('Load?: '))
        else:
            word = [reg.bits[i].dff.master.state() for i in range(reg.size)]
            print(reg.state())
        reg.update(word, load, tick)
        print()
        tick = 1 - tick
        
if __name__ == '__main__':
    test()






