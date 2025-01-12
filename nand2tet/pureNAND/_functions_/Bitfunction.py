import Mux
import DFF


qm = '0'
qs = '0'

clock = 0

def Bit(d, e, qs, load):
   sub = Mux(d, qs, load)
   qm, qs = DFF(sub, e, qm, qs)
   return (qm, qs) 
   

