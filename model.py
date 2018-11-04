import numpy as np
from genetic import Gene

input_size = Gene.input_size
hidden_size = Gene.hidden_size

def forward_model(A, x, C):
    return np.tanh(np.dot(A, x)+C)



def nn(A, B, C, D, x):
    return np.tanh(np.dot(C, np.matmul(A, x) + B) + D)


def format_weight_array(array):
    A = np.array(array[:hidden_size*input_size]).reshape((hidden_size, input_size))
    B = np.array(array[hidden_size*input_size:hidden_size*(input_size+1)])
    C = np.array(array[hidden_size*(input_size+1):hidden_size*(input_size+2)])
    D = np.array(array[hidden_size*(input_size+2)])
    return A, B, C, D

