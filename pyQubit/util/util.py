from .. import  math
import numpy as np

def qubit_coefficient(bit):
   rate = math.array.rated_ndarray(pow(2,bit))
   return math.complex.fixednorm_randComplex(np.sqrt(rate))

def fixed_qubit_coefficient(bit,i):
    # i番目の係数の絶対値の2条が1
    base = np.zeros(pow(2,bit),int)
    index = 0
    if type(i) == 'int':
        index = i
    elif type(i) == 'str':
        index = int(i,2)

    base[index] = 1
    return math.complex.fixednorm_randComplex(base)

def measure_qubit(array):
    # 係数の絶対値の2条の配列をroulette関数に
    return math.array.roulette(pow(np.abs(array),2))
