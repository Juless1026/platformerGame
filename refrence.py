import sys, pygame, random
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
size = width, height = 500, 288
background = pygame.image.load("Map.png")
bgrect = background.get_rect()

screen = pygame.display.set_mode(size)
pframes = 6
playerrun = []
playerrunL = []
i = 1
while i <= 6:
	playerrun.append(pygame.image.load("hero-run-"+str(i)+".png"))
	playerrunL.append(pygame.image.load("hero-run-"+str(i)+"l.png"))
	i +=1
playeridle = pygame.image.load("hero1.png")
player = playeridle
playerrect = player.get_rect()

heart = pygame.image.load("heart.png")
heartrect = heart.get_rect()
heartrect.bottom = random.randint(20,258)
heartrect.left = random.randint(0,1425)


fullscreen = pygame.image.load("Map.png")
fullscreenrect = fullscreen.get_rect()

font = pygame.font.SysFont("freesansbold.ttf", 60)


pygame.key.set_repeat(1,10)

ypos= 0
yspeed = 0
g = 900
hearts=0
run_i = 0
count = 0
while True:
	statustext = font.render(str(hearts), False, (0,0,0))
	print (hearts)
	clock.tick()
	fps = clock.get_fps()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_w:
				if not up:
					yspeed = -650
					up=True
			if event.key == pygame.K_a:
				playerrect=playerrect.move(-8,0)
				player = playerrunL[run_i]
				if count % 6 == 0:
					run_i = (run_i + 1) % 6
			if event.key == pygame.K_d:
				playerrect=playerrect.move(8,0)
				player = playerrun[run_i]
				if count % 6 == 0:
					run_i = (run_i + 1) % 6
		elif event.type == pygame.QUIT:
			sys.exit()
		else:
			player = playeridle

	if playerrect.bottom<=258 and fps != 0:
		yspeed += g / fps
		playerrect=playerrect.move(0,(yspeed / fps) + (g / (fps * fps * 2)))
	elif yspeed<=0.01:
		yspeed = 0
		playerrect.bottom = 258
		up=False
	else:
		up=False


	if playerrect.colliderect(heartrect):
		heartrect.bottom = random.randint(20,258)
		heartrect.left = random.randint(0,1425)
		hearts += 1

	
	fullscreen.fill(0)
	fullscreen.blit(background, bgrect)
	fullscreen.blit(player, playerrect)
	fullscreen.blit(heart,heartrect)

	screen.fill(0);
	templeft = -playerrect.left + width/2 - playerrect.width/2


	if templeft > 0:
		fullscreenrect.left=0
	elif -templeft + width >= fullscreenrect.width:
		fullscreenrect.right = width
	else:
		fullscreenrect.left=templeft
		
	screen.blit(fullscreen, fullscreenrect)
	screen.blit(statustext, statustext.get_rect())
	pygame.display.flip()
	count = (count + 1) % 600