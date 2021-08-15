from .. import  math
import numpy as np

def qubit_coefficient(bit):
   rate = math.array.rated_ndarray(pow(2,bit))
   return math.complex.fixednorm_randComplex(np.sqrt(rate))
