from Register import Register


program = './program.txt'

with open(program) as f:
    binary = [line.strip() for line in f.readlines()]
    

print(binary)


reg = Register()
line = [int(_) for _ in binary[0]]
reg.update(line, 1, 0)
reg.update(line, 1, 1)
print(reg.state())
