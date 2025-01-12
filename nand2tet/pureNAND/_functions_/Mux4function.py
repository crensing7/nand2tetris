from Mux import Mux


def Mux4Way(in1, in2, in3, in4, sel):
    first = sel[0]
    second = sel[1]
    out1 = Mux(in1, in3, first) 
    out2 = Mux(in2, in4, first) 
    outFinal = Mux(out1, out2, second)
    return outFinal
