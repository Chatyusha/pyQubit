import numpy as np
from . import inf

def rated_ndarray(size: int):
  ary = np.random.randint(0,inf.maxint,size)
  return ary / np.sum(ary)

def roulette(array):
    pin = np.random.random()
    pinindex=0
    sum = 0
    for i in array:
        sum += i
        if sum >= pin:
            return pinindex
        else:
            pinindex += 1
