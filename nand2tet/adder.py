def adder(a, b):
    total = []
    carry = 0
    for i in range(1, len(a) + 1):
        x = (a[-i] ^ b[-i])
        n = (a[-i] & b[-i])
        o = (a[-i] | b[-i])
        add = (x & ~carry) | (~x & carry)
        carry = (n & ~carry) | (o & carry)
        total.append(add)
    return total[::-1]
