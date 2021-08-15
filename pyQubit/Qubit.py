import numpy as np
from .math import inf
from .util import util
import cmath

class Qubit ():
    # self.bit --> size of bit
    def __init__(self,bit: int):
        self.bit = bit
        self.coeff = util.qubit_coefficient(bit)
    

