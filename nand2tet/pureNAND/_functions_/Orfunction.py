from Not import Not
from And import And


def Or(in1, in2):
	out = ''
	for sub1, sub2 in zip(str(in1), str(in2)):
		out += Not(And(Not(sub1), Not(sub2)))
	return out
