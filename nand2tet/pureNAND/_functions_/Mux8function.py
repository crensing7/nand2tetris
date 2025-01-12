from Mux import Mux
from Mux4Way import Mux4Way


def Mux8Way(in1, in2, in3, in4, in5, in6, in7, in8, sel):
    first = sel[0]                                     
    second = sel[1]
    third = sel[2]
    out1 = Mux4Way(in1, in3, in5, in7, first + second) 
    out2 = Mux4Way(in2, in4, in6, in8, first + second) 
    outFinal = Mux(out1, out2, third)
    return outFinal
