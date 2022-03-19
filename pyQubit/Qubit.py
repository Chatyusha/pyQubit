from .util import util
from .util import alogorithm
import numpy as np


class Qubit():
    def __init__(self, bit,):
        self.bit = bit

        # private methods
        self.__coeff = util.qubit_coefficient(self.bit)

    # 量子ビットの観測
    def observe(self,alg="BinarySearch"):
        if alg == "BinarySearch":
            return alogorithm.weighted_random_samplings_binary_search(self.__probabilities())
        else:
            pass
        
    # 確率振幅<-外からは分からない
    def __probabilities(self):
        return np.power(np.abs(self.__coeff),2)
    
    # デバッグ用
    def ___debug___(self):
        print("----GLOBALS----")
        print(f"valiable-bit = {self.bit}")
        print("----PRIVATES----")
        print(f"valiable-__coeff = {self.__coeff}")
        print(f"function-__probabilities = {self.__probabilities()}")


    def __doc__(self):
        pass
