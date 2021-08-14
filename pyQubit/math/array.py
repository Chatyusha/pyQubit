import numpy as np
from . import inf

def rated_ndarray(size: int):
  ary = np.random.randint(0,inf.maxint,size)
  return ary / np.sum(ary)
