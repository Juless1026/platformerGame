import pygame,sys
from time import sleep
pygame.init()
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball,(20,20))
ballrect = ball.get_rect()
screen =  pygame.display.set_mode((500,288))
xSpeed= 1
ySpeed=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect=ballrect.move(xSpeed,ySpeed)
    sleep(0.1)
    screen.fill(0)
    screen.blit(ball,ballrect)
    pygame.display.flip()
