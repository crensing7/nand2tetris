destination = {
    '0': 0b000,
    'd': 0b010,
    'a': 0b100, 
    'm': 0b001
}

location = {
    'null': 0b000,
    'jgt': 0b001, 
    'jeq': 0b010, 
    'jge': 0b011, 
    'jlt': 0b100, 
    'jne': 0b101, 
    'jle': 0b110, 
    'jmp': 0b111
}

computation = {
    '0'  : 0b101010,
    '1'  : 0b111111,
    '-1' : 0b111010,
    'd'  : 0b001100,
    'a'  : 0b110000,
    'm'  : 0b110000,
    '!d' : 0b001101,
    '!a' : 0b110001,
    '!m' : 0b110001,
    '-d' : 0b001111,
    '-a' : 0b110011,
    'd+1': 0b011111,
    'a+1': 0b110111,
    'm+1': 0b110111,
    'd-1': 0b001110,
    'a-1': 0b110010,
    'm-1': 0b110010,
    'd+a': 0b000010,
    'd+m': 0b000010,
    'd-a': 0b010011,
    'd-m': 0b010011,
    'a-d': 0b000111,
    'm-d': 0b000111,
    'd&a': 0b000000,
    'd&m': 0b000000,
    'd|a': 0b010101,
    'd|m': 0b010101,
}

symbols = {
    'r0': 0b0000000000000000, 
    'r1': 0b0000000000000001, 
    'r2': 0b0000000000000010, 
    'r3': 0b0000000000000011, 
    'r4': 0b0000000000000100, 
    'r5': 0b0000000000000101, 
    'r6': 0b0000000000000110, 
    'r7': 0b0000000000000111, 
    'r8': 0b0000000000001000, 
    'r9': 0b0000000000001001, 
    'r10': 0b0000000000001010, 
    'r11': 0b0000000000001011, 
    'r12': 0b0000000000001100, 
    'r13': 0b0000000000001101, 
    'r14': 0b0000000000001110, 
    'r15': 0b0000000000001111, 
    'screen': 0b0100000000000000,
    'kbd': 0b0110000000000000,
    'sp': 0b0000000000000000, 
    'lcl': 0b0000000000000001, 
    'arg': 0b0000000000000010, 
    'this': 0b0000000000000011, 
    'that': 0b0000000000000100
}


def transSym(word):
    return format(symbols[word.lower()], '016b')
    

def transDest(word):
    out = 0b000 
    for letter in word:
        temp = destination[letter.lower()]
        out |= temp
    return format(out, '03b')


def transJump(word):
    return format(location[word.lower()], '03b')


def transComp(word):
    return format(computation[word.lower()], '06b')





if __name__ == '__main__':
    test = 'this'
    if test in symbols.keys():
        print('yes')

