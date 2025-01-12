from Not import Not
from And import And


def Nor(in1, in2):
	out = And(Not(in1), Not(in2))
	return out
