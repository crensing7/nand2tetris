from Register import Register
from Gates import Inc


class Counter():
    def __init__(self):
        self.ct = Register()
    
    def inc(self, clock):
        self.ct.update(Inc(self.ct.state()), 1, clock)

    def set(self, word, clock):
        self.ct.update(word, 1, clock)

    def reset(self, clock):
        for i in range(self.ct.size):
            self.ct.bits[i].update(0, 1, clock) 

    def state(self):
        return self.ct.state()


def test():
    counter = Counter()
    tick = 0
    while True:
        if tick == 0:
            choice = input('Inc/Set/Reset? ')
            if choice == 'i':
                counter.inc(tick)
            if choice == 's':
                word = [int(_) for _ in input('Word?: ')]
                counter.set(word, tick)
            if choice == 'r':
                counter.reset(tick)
        if tick == 1:
            counter.inc(1)
            counter.reset(1)
            counter.set([0] * 16, 1)
            print(counter.state())
        tick = 1 - tick

if __name__ == '__main__':
    test()
          



