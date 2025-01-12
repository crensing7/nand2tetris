from Nor import Nor
from And import And
from Not import Not
from Or import Or


def Dextra(d, e, pre, clr, q0):
	se = And(d, e)
	re = And(Not(d), e)

	p = Nor(se, q0)
	clear = Or(clr, p)

	q = Nor(re, clear)
	preset = Or(pre, q)
	
	return (preset, clear)



q0 = '1'

while True:
	sel = input()
	sel2 = input()
	d = sel[0] 
	e = sel[1]
	pre = sel2[0] 
	clr = sel2[1] 
	q0 = Dextra(d, e, pre, clr, q0)[0]
	print(Dextra(d, e, pre, clr, q0))	
