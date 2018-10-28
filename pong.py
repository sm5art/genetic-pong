import pygame,sys
from pygame.locals import*
from paddle_object import paddle
from ball import Ball
import random
import pandas as pd
import math
pygame.init()


WIDTH = 858
HEIGHT = 525
SPACING = 25
P_LENGTH = 100
P_WIDTH = 15
P_SPEED = 10
MAXBOUNCEANGLE = math.pi/4
MAXSPEED = 10
screen = pygame.display.set_mode((WIDTH,HEIGHT))

gen = pd.read_csv('gen15.csv')
a = gen.sort_values('fitness').iloc[-1][['a1', 'a2', 'a3', 'a4', 'a5']]
print("USING WEIGHTS")
print(a)
two = paddle(screen,WIDTH-SPACING-P_WIDTH,HEIGHT/2-P_LENGTH/2,P_LENGTH,P_WIDTH,'two',P_SPEED, weights=a)
one = paddle(screen,SPACING,HEIGHT/2-P_LENGTH/2,P_LENGTH,P_WIDTH,'one',P_SPEED)
ball = Ball(screen,WIDTH/2,HEIGHT/2,20, 50,50, color=(255,255,255))



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

def reset(x,bool):
	ball.x = WIDTH/2
	ball.y = HEIGHT/2
	if x:
		ball.x_speed = 5
		ball.y_speed = random.choice([-5,5])
	else:
		ball.x_speed = -5
		ball.y_speed = random.choice([-5,5])

	if bool:
		one.x=WIDTH-SPACING-P_WIDTH
		two.x=SPACING
		one.y=HEIGHT/2-P_LENGTH/2
		two.y=HEIGHT/2-P_LENGTH/2

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
	reset(random.choice([True,False]),True)
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
		
		one.move_kb()
		two.move_ai(ball)
		"""if random.randint(0,1) == 0:
			one._move_up()
		else:
			one._move_down()
		one._draw()"""
		ball.move()

		
		#if ball touches left wall
		if (ball.x <= 0):
			two_score.play()
			two_pt+=1
			reset(False,False)

		#if ball touches right wall
		if (ball.x+ball.size >= WIDTH):
			one_score.play()
			one_pt+=1
			reset(False,False)  
		

		if (one_pt == 10):
			win("Player 1")
		elif (two_pt == 10):
			win("Player 2")


		
			
		#collisions	
		if ball.collide(pygame.Rect(one.x,one.y,one.width,one.length)):
			one_sound.play()
			ball.bounce(MAXSPEED,MAXBOUNCEANGLE,one)
			
			#ball.bounce(ball_v,"one")
			#ball.bounce_normal(808,ball_v,one)

		elif ball.collide(pygame.Rect(two.x,two.y,two.width,two.length)):
			two_sound.play()
			ball.bounce(MAXSPEED,MAXBOUNCEANGLE,two)
		
		print_f(str(one_pt),100,(255,255,255),WIDTH/4,150)
		print_f(str(two_pt),100,(255,255,255),WIDTH/2 + WIDTH/4,150)



		clock.tick_busy_loop(FPS)
		pygame.display.update()

play()