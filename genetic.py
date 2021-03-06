import random
import numpy as np

"""
fitness = # num of times it bounces
A chromosome which expresses a possible solution to the problem as a string
A fitness function which takes a chromosome as input and returns a higher value for better solutions (much more likely to reproduce)
A population which is just a set of many chromosomes
A selection method which determines how parents are selected for breeding from the population
A crossover operation which determines how parents combine to produce offspring
A mutation operation which determines how random deviations manifest themselves
"""

#state = ( delta_y_ball/delta_x_ball                 range: (-1 to 1)
#           (y_ball-y_paddle)/height                 range: (-1 to 1)
#                   y_paddle/height                  range (0 to 1)    
#             x_ball/width                           range (0 to 1))

#output = # -1 0 1 scalar which way to go

#linear model 
# tanh(A*inputs) = output
# (1x4) * (4x1) = (1x1)
# A = (a1 a2 a3 a4) lets create a linear constraint where a has a possible value between (-1 to 1)

#inital population is randomly generated A's
#we then run through each one calculate fitness
"""
Gene class contains a class to represent a pong paddle's alleles and to easily convert them 
to decimal numbers so that you can use the values in inference as well as in training the algo
w/ crossover and mutation.
"""
class Gene(object):
    n = 8 # how many alleles should I use to represent one number 
    hidden_size = 16 # how many hidden layer you want, positively correlated w/ size of allele
    input_size = 4 # how many inputs there are, positively correlated w/ size of allele
    var = input_size*hidden_size + 2*hidden_size + 1 # total number of variables to account for based on NN model
    weight_min = -1
    weight_max = 1
    def __init__(self, alleles=None):
        if alleles:
            self.alleles = alleles
        else:
            self.alleles = [random.randint(0, 1) for i in range(Gene.var*Gene.n)]

    # get decimal number array of length var from binary allele representation
    def numpy_values(self):
        vals = []
        for i in range(Gene.var): # the next line looks really complicated but all it does is convert to binary
            vals.append(          # and then normalize between weight_min and weight_max
                int("".join(
                    [str(g) for g in self.alleles[i*Gene.n:(i+1)*Gene.n]]), 2) 
                * (Gene.weight_max-Gene.weight_min)/2**Gene.n + Gene.weight_min )
        return np.array(vals)

    # default chance of mutation is 1%
    def _mutate(self, alleles, chance=0.01):
        new_alleles = []
        for i in range(Gene.var*Gene.n):
            if random.random() < chance and i % Gene.n != 0:
                stored = new_alleles.pop()
                new_alleles.append(alleles[i])
                new_alleles.append(stored)
            else:
                new_alleles.append(alleles[i])
        return new_alleles



    def _crossover(self, other):
        alleles = []
        for i in range(Gene.var*Gene.n):
            if random.randint(0, 1) > 0:
                alleles.append(self.alleles[i])
            else:
                alleles.append(other.alleles[i])
        alleles = self._mutate(alleles)
        return Gene(alleles=alleles)

    #returns list of children (Gene object)
    # crossover will create crossover with the self and other for a total of n_children times 
    # returns a list of Genes in size n_children
    def crossover(self, other, n_children=50):
        lst = []
        for i in range(n_children):
            lst.append(self._crossover(other))
        return lst


    
