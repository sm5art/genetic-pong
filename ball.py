import pygame
import math
from paddle_object import paddle
import random
pygame.init()

WIDTH = 858
HEIGHT = 525



class Ball(object):
	
	def __init__(self, screen,x,y,size,x_speed,y_speed, color):
		
		self.screen = screen
		self.x = x
		self.y = y
		self.size = size
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.color = color

	def move(self):
		self.x+=self.x_speed
		self.y+=self.y_speed
		if (self.y <= 0 and self.y_speed < 0):
			self.y_speed = -self.y_speed
		elif (self.y+self.size >= HEIGHT and self.y_speed > 0):
			self.y_speed = -self.y_speed
		self._draw()

	def _draw(self):
		pygame.draw.rect(self.screen, self.color,[self.x,self.y,self.size,self.size])

	# TODO: FIX THIS TOMOOROOW
	def bounce(self,speed,angle,padd, train=False):
		if train:
			normalY = random.random()*2-1
		else:
			relativeY = -self.y - self.size/2 + padd.y + padd.length/2
			normalY = relativeY/(padd.length/2)
		theta = normalY*angle
		if self.y > HEIGHT - self.size*3 and theta == 0:
			print("weird collision on bottom")
			if (padd.player == 'one'):
				theta = 0.1
			else:
				theta = -0.1
		elif self.y <= self.size*3 and theta == 0:
			if (padd.player == 'one'):
				theta = 0.1
			else:
				theta = -0.1
			print("weird collision on top")
		if (padd.player == 'one'):
			self.x_speed = -math.cos(theta)* speed
			self.y_speed = -math.sin(theta)* speed
		else:
			self.x_speed = math.cos(theta)* speed
			self.y_speed = -math.sin(theta)* speed


		

	def collide(self,other):
		return other.colliderect(pygame.Rect(self.x,self.y,self.size,self.size))


