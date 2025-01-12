from Mux import Mux
from Not import Not


def xctrl(inx, zx, nx):
	xctrl = ''
	bitout = ''
	zxout = ''
	nxout = ''
	for bitx in inx:
		bitout += bitx
		zx1 = Mux(bitx, '0', zx)	
		zxout += zx1
		nx1 = Mux(zx, Not(zx), nx)	
		nxout += nx1
		xctrl = nxout
	print(bitout)
	print(zxout)
	print(nxout)
	print(xctrl)


zx = '0'
nx = '0'

x = '1111111111111111'

xctrl(x, zx, nx)
