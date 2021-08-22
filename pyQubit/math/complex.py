import numpy as np
from . import inf

def fixednorm_randComplex(norm,bit=1):
    base = norm + 0j
    rand = np.random.uniform(0.0,2*np.pi,bit)
    return base * (np.cos(rand)+(1j)*np.sin(rand))

def pair_complex():
    rand_sq = np.random.randint(0,inf.maxint,2)
    base = np.sqrt(rand_sq / np.sum(rand_sq))
    rand_angle = np.random.uniform(0.0,2*np.pi,2)
    return base * (np.cos(rand_angle)+(1j)*np.sin(rand_angle))


