from train import Train
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
        self.train_paddles = []
        self.dead = False
        for i in range(self.P):
            color = [100, 100, 100]
            mod = i%3
            color[mod] = 5*i
            a = Train(color, screen,SPACING,random.randint(0, HEIGHT),P_LENGTH,P_WIDTH,'two',P_SPEED)
            a.one = right_paddle
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

    # this method returns a new generation of those who had the best fitness of the dead paddles
    # it choses the highest two fitness scores and crossbreeds these two
    #def selection(self):
