from DFF import DFF


qm = '0'
qs = '0'

while True:
	sel = input()
	d = sel[0]
	e = sel[1]
	qm = DFF(d, e, qm, qs)[0]
	qs = DFF(d, e, qm, qs)[2]
	print(DFF(d, e, qm, qs)[0:2])
	print(DFF(d, e, qm, qs)[2:4])
