from Nor import Nor
from And import And
from Not import Not


def Dgated(d, e, q0):
	se = And(d, e)
	re = And(Not(d), e)
	p = Nor(se, q0)
	q = Nor(re, p)
	return (q, p)



q0 = '1'

while True:
	sel = input()
	d = sel[0] 
	e = sel[1] 
	q0 = Dgated(d, e, q0)[0]
	print(Dgated(d, e, q0))	
