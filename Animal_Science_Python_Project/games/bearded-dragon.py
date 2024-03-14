import pygame
pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)
black = (0,0,0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bearded Dragon")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(white)
    pygame.display.flip()
    clock.tick(60)