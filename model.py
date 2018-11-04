import numpy as np

def forward_model(A, x, C):
    return np.tanh(np.dot(A, x)+C)



def nn(A, B, C, D, x):
    return np.tanh(np.dot(C, np.matmul(A, x) + B) + D)


def format_weight_array(array):
    A = np.array(array[:12]).reshape((3, 4))
    B = np.array(array[12:15])
    C = np.array(array[15:18])
    D = np.array(array[18])
    return A, B, C, D

