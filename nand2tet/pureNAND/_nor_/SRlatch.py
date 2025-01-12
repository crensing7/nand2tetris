from Nor import Nor


def SRlatch(s, r, q0):
	p = Nor(s, q0)
	q = Nor(r, p)
	return (q, p)



q0 = '0'

while True:
	sel = input()
	s = sel[0]
	r = sel[1]
	q0 = SRlatch(s, r, q0)[0]
	print(SRlatch(s, r, q0))
