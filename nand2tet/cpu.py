from alu import alu
from mem import rom, ram
from conv import b2d


class cpu:
    def __init__(self, romSize, ramSize):
        self.romSize = romSize
        self.dReg = rom(1)
        self.aReg = rom(1)
        self.pc   = 0 
        self.rom  = rom(romSize)
        self.ram  = ram(ramSize)
      

    def reset(self): 
        self.rom.load()
        self.pc = 0


    def fetch(self):
        print(self.pc)
        self.rom.addr(self.pc) 
        instruction = self.rom.state()
        mode = instruction[0]
        self.pc = (self.pc + 1) % self.romSize
        return instruction, mode


    def aInst(self, instruction):
        print(f'A Instruction: {instruction}')
        self.aReg.update([0] + instruction[1:])
        self.rom.addr(b2d(instruction[1:]))
        self.ram.addr(b2d(instruction[1:]))
        
   
    def cInst(self, instruction):
        switch  = instruction[3]
        control = instruction[4:10]
        dest    = instruction[10:13]
        jump    = instruction[13:16]
        print(f'C Instruction: {instruction[:3]}, {[switch]}, {control}, {dest}, {jump}')
        a = []
        if switch == 0:
            a = self.aReg.state()
        else:
            a = self.ram.state()
        self.ram.addr(b2d(self.aReg.state()))
        d = self.dReg.state()
        out, zr, ng = alu(d, a, control)
##        print(f'Computation: {out}, {ng}, {zr}, {1 - (ng | zr)}')

        ## Dest
        if dest[0]:
            self.aReg.update(out)
        if dest[1]:
            self.dReg.update(out)
        if dest[2]: 
            self.ram.update(out)

        ## Jump
        condition = 0
        if jump[0]:
            condition |= ng
        if jump[1]:
            condition |= zr
        if jump[2]:
            condition |= 1 - (ng | zr)
        if condition > 0:
            self.pc = b2d(self.aReg.state())


    def execute(self, instruction, mode):
        if mode == 0:
            self.aInst(instruction)
        if mode == 1:
            self.cInst(instruction)

    def cycle(self):
        instruction, mode = self.fetch()
        self.execute(instruction, mode)
            
   
## if __name__ == '__main__':
##     cpu = cpu(100, 24577)      
##     cpu.reset()
##     while True:
##         cpu.cycle()
##         print(cpu.ram.screen())
##         print(cpu.ram.cache)
##         check = input('Continue?')

if __name__ == '__main__':
    cpu = cpu(32768, 24577)      
    cpu.reset()
    while True:
        print('-' * 80)
        print(f'PC: {cpu.pc + 1}')
        cpu.cycle()
        print('A Register')
        print(cpu.aReg.state())
        print('D Register')
        print(cpu.dReg.state())
        print('ROM Select')
        print(cpu.rom.selected)
        print('RAM Select')
        print(cpu.ram.selected)
        print('RAM')
        cpu.ram.full()
##        print(cpu.ram.cache[:2])
        check = input('Continue?')














