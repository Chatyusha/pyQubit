import numpy as np
from . import math
from .util import gates


class unitQubit():
    def __init__(self, default=None):
        #        if init:
        #            self.coef = math.complex.pair_complex(np.array([1, 0]))
        #        else:
        #            self.coef = math.complex.pair_complex()

        # 初期値が指定なし -> ランダム
        if default is None:
            self.coef = math.complex.pair_complex()
        else:
            self.coef = math.complex.pair_complex(default)
        self.alpha = self.coef[0]
        self.beta = self.coef[1]

    def init(self, default=np.array([1, 0])):
        self.__init__(default)


class Qubit():
    def __init__(self, bit, zeroinit=False, default=None):
        self.bit = bit
        if zeroinit:
            ary = [unitQubit(default=np.array([1, 0])) for i in range(bit)]
        elif default is None:
            ary = [unitQubit() for i in range(bit)]
        else:
            ary = [unitQubit(i) for i in default]

        self.qbits = np.array(ary)
        base = np.array(np.abs([i.coef for i in self.qbits])**2)

        # 2進数の位
        bindigit = np.array([2**i for i in range(bit)])
        # 最大値まで
        flags = np.array([i for i in range(2**bit)])

        # xのbitが立っている部分の配列
        def F(x):
            return np.array([1 if i > 0 else 0 for i in x & bindigit])

        # 0~最大値まで、それぞれの数のbitが立っている場所
        selected = np.array([F(i) for i in flags])

        # |L>の確率
        def G(L):
            r = 1
            for i, j in zip(range(bit), L):
                r *= base[i][j]

            return r

        self.rate = np.array([G(i) for i in selected])
        self.coefs = math.complex.fixednorm_randComplex(
            np.sqrt(self.rate), 2**bit)

    def init(self, zeroinit=True):
        self.__init__(self.bit, zeroinit=zeroinit)
