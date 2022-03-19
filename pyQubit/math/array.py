import numpy as np
from . import inf


def rated_ndarray(size: int) -> np.ndarray:
    base = np.random.randint(0, inf.maxint, size)
    return base / np.sum(base)


def roulette(array) -> int:
    pin = np.random.random()
    pinindex = 0
    sum = 0
    for i in array:
        sum += i
        if sum >= pin:
            return pinindex
        else:
            pinindex += 1
