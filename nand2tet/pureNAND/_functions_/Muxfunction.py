from Not import Not
from And import And
from Or import Or


def mux(inputs, sel):
    return Or(And(inputs[0], Not(sel)), And(inputs[1], sel)) 

def mux4(inputs, sel):
    first = mux([inputs[0], inputs[1]], sel[1])
    second = mux([inputs[2], inputs[3]], sel[1])
    return mux([first, second], sel[0]) 

def mux8(inputs, sel):
    first = mux4([inputs[0], inputs[1], inputs[2], inputs[3]], sel[1:3])
    second = mux4([inputs[4], inputs[5], inputs[6], inputs[7]], sel[1:3])
    return mux([first, second], sel[0])


def test():
    while True:
        choice = input('1, 4, 8?: ')
        inputs = input('Input: ')
        sel = input('Selector: ')
        if choice == '1':
            print(mux(inputs, sel))
        if choice == '4':
            print(mux4(inputs, sel))
        if choice == '8':
            print(mux8(inputs, sel))

if __name__ == '__main__':
    test()






