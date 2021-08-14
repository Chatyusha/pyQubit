import numpy as np
import cmath
import math

def fixednorm_randComplex(norm:int):
    base = norm + 0j
    rand = np.random.uniform(0.0,2*np.pi)
    return base * (math.cos(rand)+(1j)*math.sin(rand))

