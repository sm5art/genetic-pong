from paddle_object import paddle
from genetic import Gene, forward_model
import numpy as np
from ball import Ball
import random
import pygame
import math

MAXBOUNCEANGLE = math.pi/4
MAXSPEED = 10

WIDTH = 858
HEIGHT = 525

class Train(object):
    def __init__(self, color, screen,x,y,length,width,player,speed, gene=None):
        self.color = color
        self.paddle = paddle(screen,x,y,length,width,player,speed)
        self.ball = Ball(screen,WIDTH/2,HEIGHT/2,20,5,random.randint(-5, 5), color)
        self.dead = False
        self.fitness = 0
        if gene:
            self.g = gene
            self.A = self.g.numpy_values()
        else:
            self.g = Gene()
            self.A = self.g.numpy_values()

    def move(self, decision):
        if decision > 0.0:
            self.paddle._move_up()
        elif decision < 0.0:
            self.paddle._move_down()
        self.paddle._draw(color=self.color)

    def on_update(self):
        if self.dead:
            return
        self.ball.move()
        if (self.ball.x <= 0):
            self.dead = True
            return
        if self.check_collision(self.paddle):
            self.fitness += 1
        self.check_collision(self.one)
        X = prepare_features(self.ball.x_speed, self.ball.y_speed, self.ball.y, self.paddle.y, self.ball.x)
        self.move(forward_model(self.A, X))

    def check_collision(self, paddle):
        if self.ball.collide(pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.length)):
            self.ball.bounce(MAXSPEED,MAXBOUNCEANGLE, paddle)
            return True
        return False

    def reset(self):
        self.ball.x = WIDTH/2
        self.ball.y = HEIGHT/2
        self.ball.x_speed = 5
        self.ball.y_speed = random.choice([-5,5])

def prepare_features(ball_dx, ball_dy, y_ball, y_paddle, x_ball):
    return np.array([ball_dy/MAXSPEED, ball_dx/MAXSPEED, (y_ball-y_paddle)/HEIGHT, y_paddle/HEIGHT, x_ball/WIDTH])
        
