import numpy as np

def Xgate(coeff):
    base=np.array([[0,1],[1,0]])
    return np.dot(base,coeff)

def Zgate(coeff):
    base = np.array([[1,0],[0,-1]])
    return np.dot(base,coeff)
