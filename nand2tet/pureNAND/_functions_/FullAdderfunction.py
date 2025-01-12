from Xor import Xor
from And import And
from Mux import Mux
from Not import Not
from Or import Or


def FullAdder(in1, in2, carry):
	sum1 = Mux((Xor(in1, in2)), (Not(Xor(in1, in2))), carry)
	carry = Mux((And(in1, in2)), (Or(in1, in2)), carry)
	return (sum1, carry)
