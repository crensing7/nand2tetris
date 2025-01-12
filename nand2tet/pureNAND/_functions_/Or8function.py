from Or import Or


def Or8Way(in1):
	out1 = '0'
	for bit in range(0, len(in1)):
		out1 = Or(out1, in1[bit])
	return out1
