from Register import Register
from Counter import Counter
from ROM32K import ROM32K












class CPU():
    def __init__(self):
        self.aReg = Register()
        self.dReg = Register()  
        self.counter = Counter() 

    def fetch(self, clock):
        


    
cpu = CPU()    
print(cpu.aReg.state())
print(cpu.dReg.state())
print(cpu.counter.state())

