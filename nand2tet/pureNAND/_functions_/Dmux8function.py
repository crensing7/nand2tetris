from Dmux import Dmux
from Dmux4Way import Dmux4Way


def Dmux8Way(in1, sel):
    first = sel[0]
    second = sel[1]
    third = sel[2]
    upper, lower = Dmux(in1, first)
    out1, out2, out3, out4 = Dmux4Way(upper, second + third)
    out5, out6, out7, out8 = Dmux4Way(lower, second + third)
    return [out1, out2, out3, out4, out5, out6, out7, out8]
