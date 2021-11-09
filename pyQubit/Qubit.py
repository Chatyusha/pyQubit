from .util import util
from .math import complex
import numpy as np


class Qubit():
    def __init__(self, bit, zeroinit=False, default=None):
        self.bit = bit
        if zeroinit is True:
            self.coeff = np.zeros(2**bit, dtype=complex)
            self.coeff[0] = 1
        if default is not None:
            self.coeff = default
        self.coeff = util.qubit_coefficient(bit)

    def __doc__(self):
        pass
