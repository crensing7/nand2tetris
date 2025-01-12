from Not import Not 
from And import And
from Or import Or

def Xor(in1, in2):
    return Or(And(in1, Not(in2)), And(Not(in1), in2))
