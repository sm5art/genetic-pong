from paddle_object import paddle
from ball import Ball
import random
import pygame
import math

MAXBOUNCEANGLE = math.pi/4
MAXSPEED = 10

WIDTH = 858
HEIGHT = 525

class Train(object):
    def __init__(self, color, screen,x,y,length,width,player,speed):
        self.color = color
        self.paddle = paddle(screen,x,y,length,width,player,speed)
        self.ball = Ball(screen,WIDTH/2,HEIGHT/2,20,50,50, color)

    def draw(self):
        self.paddle.move_kb(color=self.color)

    def on_update(self):
        self.ball.move()
        self.draw()
        if (self.ball.x <= 0):
            self.reset()
        self.check_collision(self.paddle)
        self.check_collision(self.one)

    def check_collision(self, paddle):
        if self.ball.collide(pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.length)):
            self.ball.bounce(MAXSPEED,MAXBOUNCEANGLE, paddle)



    def reset(self):
        self.ball.x = WIDTH/2
        self.ball.y = HEIGHT/2
        self.ball.x_speed = 5
        self.ball.y_speed = random.choice([-5,5])
        
