
import numpy as np
from . import math

class unitQubit():
    def __init__(self):
        self.coef =  math.complex.pair_complex()
        self.alpha = self.coef[0]
        self.beta = self.coef[1]

class Qubit():
    def __init__(self,bit):
        self.bit = bit
        ary = [unitQubit() for i in range(bit)]
        self.qbits = np.array(ary)
        base = np.array(np.abs([i.coef for i in self.qbits])**2)
        
        # 2進数の位
        bindigit = np.array([2**i for i in range(bit)])
        # 最大値まで
        flags = np.array([i for i in range(2**bit)])

        # xのbitが立っている部分の配列
        def F(x):
            return np.array([1 if i>0 else 0 for i in x&bindigit])
       
        # 0~最大値まで、それぞれの数のbitが立っている場所
        selected = np.array([F(i) for i in flags])
        
        # |L>の確率
        def G(L):
            r=1
            for i,j in zip(range(bit),L):
                r *= base[i][j]

            return r
        
        rate =  np.array([G(i) for i in selected])
        self.coefs = math.complex.fixednorm_randComplex(np.sqrt(rate),2**bit)
        
