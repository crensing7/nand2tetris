from Xor import Xor
from And import And


def Inc(in1):
	rev1 = in1[::-1]
	carry = 1
	result = ''
	for bit in rev1:
		sub1 = Xor(bit, carry)
		carry = And(bit, carry)
		result += sub1	
	out = result[::-1]
	return out


def test():
    while True:
        word = input('Word: ')
        print(Inc(word))

if __name__ == '__main__':
    test()
