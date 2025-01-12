from And import And
from Xor import Xor


def HalfAdder(in1, in2):
	sum1 = Xor(in1, in2)
	carry = And(in1, in2)
	return (sum1, carry)
