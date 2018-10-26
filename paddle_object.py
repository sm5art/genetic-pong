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
		self.config = {'one': {'w': pygame.K_i, 's': pygame.K_k}, 'two': {'w':pygame.K_w, 's':pygame.K_s }}

	def _draw(self):
		pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.width,self.length])

	def _move_down(self, multiplier=1):
		if self.y+self.length<=HEIGHT:
			self.y += multiplier*self.speed
		
	def _move_up(self, multiplier=1):
		if self.y >= 0:
			self.y -= multiplier*self.speed

	def move_kb(self):
		keys = pygame.key.get_pressed()
		if keys[self.config[self.player]['w']]:
			self._move_up()
		elif keys[self.config[self.player]['s']]:
			self._move_down()
		self._draw()

	def move_ai(self, ball):
		if ball.y > self.y:
			self._move_down(multiplier=0.25)
		elif ball.y < self.y:
			self._move_up(multiplier=0.25)

		self._draw()


		


		
		
			
