import numpy as np
import cmath
from typing import Union


#   絶対値がnormの複素数の配列
def fixednorm_randComplex(norm:np.ndarray):
    base = norm + 0j
    gen = np.random.Generator(np.random.MT19937())
    rand = gen.uniform(0.0, 2*np.pi,norm.size)
    return base * (np.cos(rand)+(1j)*np.sin(rand))


def angle(_to: complex, _from: complex = 1 + 0j):
    return cmath.phase(_to) - cmath.phase(_from)
