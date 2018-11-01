import pygame,sys
from pygame.locals import*
from paddle_object import paddle
from generation import Generation
from ball import Ball
import random
import math
pygame.init()


WIDTH = 858
HEIGHT = 525
SPACING = 25
P_LENGTH = 100
P_WIDTH = 15
P_SPEED = 10
MAXBOUNCEANGLE = math.pi/4
MAXSPEED = 15
screen = pygame.display.set_mode((WIDTH,HEIGHT))


one = paddle(screen,WIDTH-SPACING-P_WIDTH,HEIGHT/2-P_LENGTH/2,HEIGHT,P_WIDTH,'one',P_SPEED)
#new_lst = []
gen = Generation(1000, one, screen)
"""for i in range(10):
	color = [100, 100, 100]
	mod = i%3
	color[mod] = 5*i
	a = Train(color, screen,SPACING,random.randint(0, HEIGHT),P_LENGTH,P_WIDTH,'two',P_SPEED)
	a.one = one
	new_lst.append(a)"""

#two = paddle(screen,SPACING,HEIGHT/2-P_LENGTH/2,P_LENGTH,P_WIDTH,'two',P_SPEED)
#ball = Ball(screen,WIDTH/2,HEIGHT/2,20,50,50)



clock = pygame.time.Clock()
FPS = 60

bounce = False

#audio
one_sound= pygame.mixer.Sound("sound/one.wav")
two_sound = pygame.mixer.Sound("sound/two.wav")
one_score = pygame.mixer.Sound("sound/one_score.wav")
two_score = pygame.mixer.Sound("sound/two_score.wav")

def print_f(msg,siz,color,x,y):
    Text = pygame.font.Font("bit5x3.ttf",siz)
    write = Text.render(msg,True,color)
    write_rect = write.get_rect()
    write_rect.center = ((x),(y))
    screen.blit(write,write_rect)



def win(player):
    color1 =  (100, 100, 100)
    color2 =  ( 60,  60, 100)
    for i in range(13):
        color1, color2 = color2, color1
        screen.fill(color1)
        print_f(player+" Won!!",32,(255,0,0),WIDTH/2,HEIGHT/2)
        pygame.display.update()
        pygame.time.wait(300)
    play()


def play():
	one.y=0
	one.x=WIDTH-SPACING-P_WIDTH
	one_pt = 0
	two_pt = 0
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		
		screen.fill((0,0,0))
		#draw stripes
		for i in range(HEIGHT):
			if i%25 == 0:
				pygame.draw.rect(screen,(255,255,255),(WIDTH/2-2,i,4,10))
		
		gen.on_update()
		one._draw()


		print_f(str(gen.generation),100,(255,255,255),WIDTH/4,150)
		#print_f(str(two_pt),100,(255,255,255),WIDTH/2 + WIDTH/4,150)

			
		clock.tick_busy_loop(FPS)
		pygame.display.update()

play()