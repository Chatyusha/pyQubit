from ..Qubit import Qubit
import numpy as np


def Xgate(inputQubit: Qubit) -> None:
    base = np.array([[0, 1], [1, 0]])
    inputQubit.coeff = np.dot(base, inputQubit.coeff)


def Zgate(inputQubit: Qubit) -> None:
    base = np.array([[1, 0], [0, -1]])
    inputQubit.coeff = np.dot(base, inputQubit.coeff)


def Hgate(inputQubit: Qubit) -> None:
    base = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]])
    inputQubit.coeff = np.dot(base, inputQubit.coeff)
