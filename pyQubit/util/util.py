from .. import  math
import numpy as np

def qubit_coefficient(bit):
   rate = math.array.rated_ndarray(2*bit)
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

def measure_qubit(array,bit):
    # 係数の絶対値の2条の配列をroulette関数に
    base=pow(np.abs(array),2)
    ret = []
    for i in range(2**bit):
        sum = 1
        for j in range(bit):
            if ((i>>j)&1):
                sum *= base[j][0]
            else:
                sum *= base[j][1]
        ret.append(sum)
    return math.array.roulette(np.array(ret))

def selected_accumulation(flag,coefs,bit):
    base = pow(np.abs(coefs),2)
    acc = 1
    for i in range(bit):
        if ((flag >> i)&1):
            acc *= base[i][1]
        else:
            acc *= base[i][0]

    return math.complex.fixednorm_randComplex(acc)
