from HalfAdder import HalfAdder
from FullAdder import FullAdder


def Adder(in1, in2):
	rev1 = in1[::-1]
	rev2 = in2[::-1]
	total = ''
	carry = '0'
	for sub1, sub2 in zip(rev1, rev2):
		sum1, carry = FullAdder(sub1, sub2, carry)
		total += str(sum1)
	out = total[::-1]
	return(out)
