from Nor import Nor
from And import And


def SRgated(s, r, e, q0):
	se = And(s, e)
	re = And(r, e)
	p = Nor(se, q0)
	q = Nor(re, p)
	return (q, p)



q0 = '1'

while True:
	sel = input()
	s = sel[0] 
	r = sel[1] 
	e = sel[2] 
	q0 = SRgated(s, r, e, q0)[0]
	print(SRgated(s, r, e, q0))	
