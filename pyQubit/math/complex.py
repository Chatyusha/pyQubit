import numpy as np
import math

def fixednorm_randComplex(norm):
    base = norm + 0j
    rand = np.random.uniform(0.0,2*np.pi)
    return base * (np.cos(rand)+(1j)*np.sin(rand))

