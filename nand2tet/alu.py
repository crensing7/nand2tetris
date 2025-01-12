from adder import adder

def alu(a, b, ctrl):

    zx = ctrl[0]
    nx = ctrl[1]
    zy = ctrl[2]
    ny = ctrl[3]
    ff = ctrl[4]
    no = ctrl[5]

    xmid = []
    for bit in a:
        z = (bit & ~zx) | (0 & zx)
        n = (z & ~nx) | (~z & nx)
        xmid.append(n)

    ymid = []
    for bit in b:
        z = (bit & ~zy) | (0 & zy)
        n = (z & ~ny) | (~z & ny)
        ymid.append(n)

    f = []
    if ff:
        f = adder(xmid, ymid)
    else:
        for i, j in zip(xmid, ymid):
            f.append(i & j)

    n = []
    if no:
        for bit in f:
            n.append(1 - bit)
    else:
        n = f

    zr = 0
    for bit in n[::-1]:
        zr = bit | zr
    ng = n[0] and 1

    return n, 1 - zr, ng


if __name__ == '__main__':
    a = [1, 1, 1, 1]
    b = [0, 0, 0, 0]
    ctrl = [0, 0, 0, 0, 1, 0]

    print(alu(a, b, ctrl))





