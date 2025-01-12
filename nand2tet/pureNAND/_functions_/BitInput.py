import time
import Bit

qm = '0'
qs = '0'

clock = 0

while True:
    print(f'Clock: {clock}')


    e = clock
    d = input('Input: ')
    load = input('Load: ')
    
    print(Bit(d, clock, qs, load))


   

