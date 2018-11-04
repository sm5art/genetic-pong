import pygame
import math
import numpy as np
from model import forward_model, nn, format_weight_array
pygame.init()

WIDTH = 858
HEIGHT = 525
MAXSPEED = 10

def prepare_features(ball_dx, ball_dy, y_ball, y_paddle):
    return np.array([ball_dy/MAXSPEED, ball_dx/MAXSPEED, (y_ball-y_paddle)/HEIGHT, y_paddle/HEIGHT])
    

class paddle(object):

    def __init__(self,screen,x,y,length,width,player,speed,weights=None):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.player = player
        self.screen = screen
        self.speed = speed
        if weights is not None:
            self.weights = np.array(weights)
        else:
            weights = np.array([1, 1, 1, 1, 1])
        self.config = {'one': {'w': pygame.K_i, 's': pygame.K_k}, 'two': {'w':pygame.K_w, 's':pygame.K_s }}

    def _draw(self, color=(255,255,255)):
        pygame.draw.rect(self.screen,color,[self.x,self.y,self.width,self.length])

    def _move_down(self, multiplier=1):
        if self.y+self.length<=HEIGHT:
            self.y += multiplier*self.speed
        
    def _move_up(self, multiplier=1):
        if self.y >= 0:
            self.y -= multiplier*self.speed

    def move_kb(self, color=(255,255,255)):
        keys = pygame.key.get_pressed()
        if keys[self.config[self.player]['w']]:
            self._move_up()
        elif keys[self.config[self.player]['s']]:
            self._move_down()
        self._draw(color=color)

    def move_ai(self, ball):
        X = prepare_features(ball.x_speed, ball.y_speed, ball.y, self.y)
        A, B, C, D = format_weight_array(self.weights)
        decision = nn(A, B, C, D, X)
        if decision > 0.01:
            self._move_up()
        elif decision < -0.01:
            self._move_down()
        self._draw()


        


        
        
            
