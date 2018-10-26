import numpy as np

"""
fitness = # num of times it bounces
A chromosome which expresses a possible solution to the problem as a string
A fitness function which takes a chromosome as input and returns a higher value for better solutions
A population which is just a set of many chromosomes
A selection method which determines how parents are selected for breeding from the population
A crossover operation which determines how parents combine to produce offspring
A mutation operation which determines how random deviations manifest themselves
"""

#state = ( delta_y_ball/delta_x_ball 
#           (y_ball-y_paddle)/height
#                   y_paddle          )

#output = # -1 0 1 scalar which way to go

#linear model 
# tanh(A*inputs) = output
# (1x6) * (6x1) = (1x1)
# A = (a1 a2 a3)

#inital population is randomly generated A's
#we then run through each one calculate fitness


class GeneticAlgo(object):
    def __init__(self):
