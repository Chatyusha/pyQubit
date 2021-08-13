import numpy as np
from .math import inf
import cmath

class Qubit ():
    # self.bit --> size of bit
    def __init__(self,bit: int):
        self.bit = bit
        coff = np.random.randint(inf.minint,inf.maxint,self.bit)
        
        self.normedcoef = coff / np.sum(coff)
        
        judge = np.array([1 if i%2==0 else -1 for i in np.random.randint(0,inf.maxint,bit)])

        self.coefficient = np.array([cmath.sqrt(i) for i in self.normedcoef]) * judge

        


