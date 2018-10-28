import pygame
import math
from paddle_object import paddle

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

		if (self.y <= 0 or self.y+self.size >= HEIGHT):
	
			self.y_speed = -self.y_speed

		self._draw()

	def _draw(self):
		pygame.draw.rect(self.screen, self.color,[self.x,self.y,self.size,self.size])

	# TODO: FIX THIS TOMOOROOW
	def bounce(self,speed,angle,padd):
		relativeY = (padd.y+(padd.length/2)) - self.y+self.size/2
		normalizedY = (relativeY / (padd.length / 2))
		bounceSpeed = normalizedY * speed
		bounceAngle = normalizedY * angle
		if (padd.player == 'one'):
			self.x_speed = -math.cos(bounceAngle)* 15
			self.y_speed = -math.sin(bounceAngle)* 15
		else:
			self.x_speed = math.cos(bounceAngle)* 15
			self.y_speed = -math.sin(bounceAngle)* 15

		

	def collide(self,other):
		return other.colliderect(pygame.Rect(self.x,self.y,self.size,self.size))


