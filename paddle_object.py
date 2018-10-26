import pygame
import math
pygame.init()

WIDTH = 858
HEIGHT = 525

class paddle(object):

	def __init__(self,screen,x,y,length,width,player,speed):
		self.length = length
		self.width = width
		self.x = x
		self.y = y
		self.player = player
		self.screen = screen
		self.speed = speed

	def _draw(self):
		pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.width,self.length])

	def _move_down(self):
		if self.y+self.length<=HEIGHT:
			self.y += self.speed
		
	def _move_up(self):
		if self.y>=0:
			self.y -= self.speed

	def move(self):
		keys = pygame.key.get_pressed()

		if self.player == 'one':
			if keys[pygame.K_i]:
				self._move_up()
			elif keys[pygame.K_k]:
				self._move_down()
		elif self.player == 'two':
			if keys[pygame.K_w]:
				self._move_up()
			elif keys[pygame.K_s]:
				self._move_down()
		self._draw()

		


		
		
			
