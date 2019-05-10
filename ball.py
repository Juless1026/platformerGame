import pygame,sys
import time as t
from datetime import *
pygame.init()
clock = pygame.time.Clock()

class objects:
    img = pygame.image.load("placeholder.png")
    rect = img.get_rect()
    speedY= 0
    speedX=1
    weight=1
ball = objects()
ball2 = objects()
ball2.img = pygame.image.load("ball.png")
ball2.img = pygame.transform.scale(ball2.img,(20,20))
ball2.rect = ball2.img.get_rect()
ball2.speedX = -1

ball.img = pygame.image.load("ball.png")
ball.img = pygame.transform.scale(ball.img,(20,20))
ball.rect = ball.img.get_rect()
ball2.rect=ball2.rect.move(990,0)
screen =  pygame.display.set_mode((1000,300))
g = 9.80665 #m/s^2
meter = 1
fps = 60
timestart = datetime.now()


def Newspeed(speed,newtons,mass):
    acceleration=newtons/mass
    speed/=meter
    speed+= acceleration/fps
    #print(speed, str(datetime.now()-timestart))
    speed*=meter
    return speed
def Gravity(mass):
    return mass*g
def Friction(thingposy,thingspeedx):
    pass #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA D = Cd * .5 * rho * V^2 * A 
def Update(buffer):
    newtonX = 0
    newtonY = 0
    newtonY += Gravity(buffer.weight)
    return Newspeed(buffer.speedX,newtonX,buffer.weight),Newspeed(buffer.speedY,newtonY,buffer.weight)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball.posX,ball.posY = ball.rect.center
    ball.speedX,ball.speedY = Update(ball)
    if ball.posY>289 and ball.speedY>0:
        ball.speedY*=-0.9
    ball2.posX,ball2.posY = ball2.rect.center
    ball2.speedX,ball2.speedY = Update(ball2)
    if ball2.posY>289 and ball2.speedY>0:
        ball2.speedY*=-0.9
    print("SpeedY",ball.speedY,"posY",ball.posY)
    ball.rect=ball.rect.move(ball.speedX,ball.speedY)
    ball2.rect=ball2.rect.move(ball2.speedX,ball2.speedY)
    clock.tick_busy_loop(fps)
    screen.fill(0)
    screen.blit(ball.img,ball.rect)
    screen.blit(ball2.img,ball2.rect)
    pygame.display.flip()