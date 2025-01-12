from Nand import Nand


class SRlatch():
    def __init__(self):
        self.q = '0'
        self.p = '1'
    
    def update(self, s, r):
        midq = Nand(s, self.p)
        midp = Nand(r, self.q)
        
        self.q = Nand(s, midp) 
        self.p = Nand(r, midq) 

    def state(self):
        return self.q, self.p 
