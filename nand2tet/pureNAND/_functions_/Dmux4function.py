from Dmux import Dmux
from And import And
from Not import Not


def Dmux4Way(in1, sel):
    first = sel[0]
    second = sel[1]
    upper, lower = Dmux(in1, second)
    out1, out3 = Dmux(upper, first)
    out2, out4 = Dmux(lower, first)
    return [out1, out2, out3, out4]
