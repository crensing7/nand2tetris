from Nand import Nand
from Not import Not


def Dlatch(d, e, q0):
	s = Nand(d, e)
	r = Nand(Not(d), e)
	p = Nand(r, q0)
	q = Nand(s, p)	
	return q, p
