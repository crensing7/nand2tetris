from Not import Not
from Dlatch import Dlatch


def DFF(d, e, qm, qs):
    qm, pm = Dlatch(d, Not(e), qm)
    qs, ps = Dlatch(qm, e, qs)
    return (qm, qs)
