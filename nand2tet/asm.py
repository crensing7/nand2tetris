import sys
from conv import d2b
import trans
from trans import symbols

labels = {}
variable = 16
output = []
count = 0

with open(f'{sys.argv[1]}') as iFile:
    raw = [line.strip() for line in iFile.readlines()]


formatted = []
for index, instruction in enumerate(raw):
    if instruction and instruction[0] != '/':
        formatted += [instruction.lower()] 

code = []
for index, instruction in enumerate(formatted):
    if instruction[0] == '(':
        labels[instruction[1:-1]] = d2b(index - count)
        count += 1
    else:
        code += [instruction]

for index, line in enumerate(code):
    print(f'{index}: {line}')
print(labels)



for instruction in code:
    ## A instruction
    if '@' in instruction: 
        if not instruction[1].isalpha():
            output.append(d2b(instruction[1:]))
        else:
            if instruction[1:] in symbols.keys():
                output.append(trans.transSym(instruction[1:]))
            elif instruction[1:] in labels.keys():
                output.append(labels[instruction[1:]])
            else:
                labels[instruction[1:]] = d2b(variable)
                variable += 1
                output.append(labels[instruction[1:]])

    ## C instruction
    else:
        temp = (instruction.replace('=', ' ').replace(';', ' ')).split()
        if '=' in instruction and ';' in instruction:
            dest, comp, jump = temp[0], temp[1], temp[2]
        elif '=' in instruction:
            dest, comp = temp[0], temp[1]
            jump = 'null'
        elif ';' in instruction:
            comp, jump = temp[0], temp[1]
            dest = '0'

        pre = ['1', '1', '1']
        if 'm' in comp:
            pre += ['1']
        else:
            pre += ['0']
        pre += trans.transComp(comp)
        pre += trans.transDest(dest)
        pre += trans.transJump(jump)
        output.append(pre)



with open (f'{sys.argv[2]}', 'w') as oFile:
    for line in output:
        oFile.writelines(line)
        oFile.writelines('\n')
