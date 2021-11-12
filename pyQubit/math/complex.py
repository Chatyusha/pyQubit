import numpy as np
import cmath
from typing import Union


def fixednorm_randComplex(norm: Union[int, float], bit: int = 1):
    base = norm + 0j
    rand = np.random.uniform(0.0, 2*np.pi, bit)
    return base * (np.cos(rand)+(1j)*np.sin(rand))


def angle(_to: complex, _from: complex = 1 + 0j):
    return cmath.phase(_to) - cmath.phase(_from)
