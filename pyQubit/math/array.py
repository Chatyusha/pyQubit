import numpy as np
from . import inf

def rated_ndarray(size: int):
    ary = np.random.randint(0,inf.maxint,size)
    dvited = ary.reshape(size//2,2)
    return (ary / np.repeat(np.sum(dvited,axis=1),2)).reshape(size//2,2)

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
