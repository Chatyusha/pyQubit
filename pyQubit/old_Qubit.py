import numpy as np
from .math import inf
from .math import array
from .util import util
import cmath

class Qubit ():
    # self.bit --> size of bit
    def __init__(self,bit: int):
        self.bit = bit
        self.coeff = util.qubit_coefficient(bit)
    
    def defined(self,i):
        self.coeff = util.fixed_qubit_coefficient(self.bit,i)

    def measure(self):
        return util.measure_qubit(self.coeff,self.bit)
