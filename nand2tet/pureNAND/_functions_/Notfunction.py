from Nand import Nand


def Not(in1):
	out = ''
	for sub1 in str(in1):
		out += Nand(sub1, sub1)
	return out
