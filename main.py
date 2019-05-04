import pygame , sys
pygame.init()
size = width, height = 500, 288

screen = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill(0)
	pygame.display.flip()