import time
from DFF import DFF


qm = '0'
qs = '0'

clock = 0
speed = 1
while True:
    print(f'Clock: {clock}')

    if clock == 0:
        d = input('Input: ')
    else:
        d = qm

    e = clock
    qm = DFF(d, e, qm, qs)[0]
    qs = DFF(d, e, qm, qs)[1]
    print(f'Master: {DFF(d, e, qm, qs)[0]}')
    print(f'Slave : {DFF(d, e, qm, qs)[1]}')
    print()

    time.sleep(speed)
    clock = 1 - clock
		
