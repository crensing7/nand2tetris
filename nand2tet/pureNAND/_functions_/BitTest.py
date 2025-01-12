from Mux import Mux
from DFF import DFF



def Bit(d, e, qm, qs, load):
    sub = Mux(d, qs, load)
    qm, qs = DFF(sub, e, qm, qs)
    return (qm, qs)


qm = '0'
qs = '0'

clock = '0'

d = '0'
load = '0'

print(Bit(d, clock, qm, qs, load))
