from Nand import Nand
from Not import Not

def And(in1, in2):
	out = ''
	str1 = str(in1)
	str2 = str(in2)
	for sub1, sub2 in zip(str1, str2):
		out += Not(Nand(sub1, sub2))
	return out
