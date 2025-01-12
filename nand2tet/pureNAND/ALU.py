from Gates import Not, And, Or, Mux, Adder

def ALU(a, b, ctrl):

    ## Extract control values	
    zx = ctrl[0] 
    nx = ctrl[1]  
    zy = ctrl[2] 
    ny = ctrl[3] 
    ff = ctrl[4] 
    no = ctrl[5] 

    ## Zero and Negate X
    xmid = [] 
    for bit in a:
        z = Mux([bit, 0], zx)
        n = Mux([z, Not(z)], nx)
        xmid.append(n)
    print(xmid)

    ## Zero and Negate Y
    ymid = [] 
    for bit in b:
        z = Mux([bit, 0], zy)
        n = Mux([z, Not(z)], ny)
        ymid.append(n)
    print(ymid)
    
    ## And/ Add/ Final Mux 
    fn = []
    for i, j in zip(xmid, ymid):
        fn.append(And(i, j))
    fa = Adder(xmid, ymid) 
    f = []
    for i, j in zip(fn, fa):
        f.append(Mux([i, j], ff))

    ## Invert output
    out = []
    for i in f:
        out.append(Mux([i, Not(i)], no))

    ## Output checks for zero or negative 
    zrTemp = 0
    for bit in out[::-1]:
        zrTemp = Or(bit, zrTemp)
    zr = [Not(zrTemp)]
    ng = [And(out[0], 1)]

    return out + zr + ng 

def test():
    a = [0, 1, 1, 1, 0, 0, 0, 0]
    b = [0, 0, 1, 0, 0, 0, 0, 0]
    ctrl = [0, 0, 0, 0, 0, 0]
    print(ALU(a, b, ctrl))

if __name__ == '__main__':
    test()









