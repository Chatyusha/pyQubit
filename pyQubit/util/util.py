from .. import math
import numpy as np


def qubit_coefficient(bit):
    # 量子ビットの係数を生成
    coeff_num = 2 ** bit
    rate = math.array.rated_ndarray(coeff_num)
    return math.complex.fixednorm_randComplex(np.sqrt(rate))


def fixed_qubit_coefficient(bit, i):
    # i番目の係数の絶対値の2条が1
    base = np.zeros(pow(2, bit), int)
    index = 0
    if type(i) == 'int':
        index = i
    elif type(i) == 'str':
        index = int(i, 2)

    base[index] = 1
    return math.complex.fixednorm_randComplex(base)


