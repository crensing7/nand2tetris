from Nand import Nand


def SRlatch(s, r, q0):
	p = Nand(r, q0)
	q = Nand(s, p)	
	return (q, p)
