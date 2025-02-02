## Standard
def Nand(a, b):
    if a:
        if b:
            return 0
        else:
            return 1
    else:
        return 1

def Not(a):
    return Nand(a, a)

def And(a, b):
    return Not(Nand(a, b))

def Or(a, b):
    return Not(And(Not(a), Not(b)))

def OrMulti(a):
    out = 0
    for bit in a:
        out = Or(out, bit)
    return out 

def Nor(a, b):
    return And(Not(a), Not(b))

def Xor(a, b):
    return Or(And(a, Not(b)), And(Not(a), b))


## Mux
def Mux(inputs, sel):
    return Or(And(inputs[0], Not(sel)), And(inputs[1], sel)) 

def Mux4(inputs, sel):
    first = Mux([inputs[0], inputs[1]], sel[1])
    second = Mux([inputs[2], inputs[3]], sel[1])
    return Mux([first, second], sel[0]) 

def Mux8(inputs, sel):
    first = Mux4([inputs[0], inputs[1], inputs[2], inputs[3]], sel[1:3])
    second = Mux4([inputs[4], inputs[5], inputs[6], inputs[7]], sel[1:3])
    return Mux([first, second], sel[0])

def Dmux(bit, sel):
    return [And(bit, Not(sel)), And(bit, sel)]

def Dmux4(bit, sel):
    upper, lower = Dmux(bit, sel[0])
    return Dmux(upper, sel[1]) + Dmux(lower, sel[1])

def Dmux8(bit, sel):
    upper, lower = Dmux(bit, sel[0])
    return Dmux4(upper, sel[1:3]) + Dmux4(lower, sel[1:3]) 

## Adder
def HalfAdder(a, b):
    return [Xor(a, b), And(a, b)]

def FullAdder(a, b, carry):
    sum1 = Mux([Xor(a, b), Not(Xor(a, b))], carry)
    carry = Mux([And(a, b), Or(a, b)], carry)
    return [sum1, carry]
    
def Adder(a, b):
    total = []
    carry = 0
    for i in range(1, len(a) + 1):
        sum1, carry = FullAdder(a[-i], b[-i], carry)
        total.append(sum1)
    return total[::-1]

def Inc(a):
    total = []
    carry = 1
    for i in a[::-1]:
        sum1, carry = HalfAdder(i, carry)
        total.append(sum1)
    return total[::-1] 









def test():
    a = 0
    print(a, Not(a))
    a = 1
    print(a, Not(a))




if __name__ == '__main__':
    test()











