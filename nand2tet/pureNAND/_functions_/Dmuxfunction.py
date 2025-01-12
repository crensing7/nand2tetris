from Not import Not 
from And import And
from Or import Or


def dmux(data, sel):
    return [And(data, Not(sel)), And(data, sel)]

def dmux4(data, sel):
    upper, lower = dmux(data, sel[0])
    return dmux(upper, sel[1]) + dmux(lower, sel[1])

def dmux8(data, sel):
    upper, lower = dmux(data, sel[0])
    return dmux4(upper, sel[1:3]) + dmux4(lower, sel[1:3]) 


def test():
    while True:
        choice = input('1, 4, 8?: ')
        data = input('Data: ')
        sel = input('Selector: ')
        if choice == '1':
            print(dmux(data, sel))
        if choice == '4':
            print(dmux4(data, sel))
        if choice == '8':
            print(dmux8(data, sel))

if __name__ == '__main__':
    test()                


