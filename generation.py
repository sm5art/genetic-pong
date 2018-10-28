from train import Train
import pandas as pd
import random

WIDTH = 858
HEIGHT = 525
SPACING = 25
P_LENGTH = 100
P_WIDTH = 15
P_SPEED = 10

class Generation(object):
    def __init__(self, initial_population, right_paddle, screen):
        self.P = initial_population
        self.right_paddle = right_paddle
        self.screen = screen
        self.generation = 0
        self.init()

    def init(self, genes=None):
        self.train_paddles = []
        self.dead = False
        self.generation += 1
        if genes:
            for i in range(len(genes)):
                color = [100, 100, 100]
                mod = i%3
                color[mod] = i
                a = Train(color, self.screen,SPACING,HEIGHT/2,P_LENGTH,P_WIDTH,'two',P_SPEED, gene=genes[i])
                a.one = self.right_paddle
                self.train_paddles.append(a)
        else:
            for i in range(self.P):
                color = [100, 100, 100]
                mod = i%3
                color[mod] = i
                a = Train(color, self.screen,SPACING,HEIGHT/2,P_LENGTH,P_WIDTH,'two',P_SPEED)
                a.one = self.right_paddle
                self.train_paddles.append(a)


    def on_update(self):
        if self.dead:
            return
        i = 0
        for paddle in self.train_paddles:
            if not paddle.dead:
                i += 1
                paddle.on_update()
        # all paddles died
        if i == 0:
            self.dead = True
            for paddle in self.train_paddles:
                print(paddle.fitness)
            if self.generation % 5 == 0:
                pd.DataFrame([list(paddle.A) + [paddle.fitness] for paddle in self.train_paddles], columns=["a1", "a2", "a3", "a4", "a5", "fitness"]).to_csv("gen%d.csv"%self.generation)
            self.selection()

    # this method returns a new generation of those who had the best fitness of the dead paddles
    # it choses the highest two fitness scores and crossbreeds these two
    def selection(self):
        if not self.dead:
            return
        new_generation = []
        fitness = [(i, paddle.fitness) for i, paddle in enumerate(self.train_paddles)]
        fitness = sorted(fitness, key=lambda x: x[1])
        fit_list = fitness[-10:]
        random.shuffle(fit_list)
        top_n = 5
        for i in range(top_n):
            myself = self.train_paddles[fit_list.pop()[0]].g
            mate = self.train_paddles[fit_list.pop()[0]].g
            son = myself.crossover(mate, n_children=20) # woah calm down there assuming genders
            new_generation += son
        self.init(genes=new_generation)



