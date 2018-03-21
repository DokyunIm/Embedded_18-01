import pygame

width = 640
height = 480
radius = 100
blank = 0

pygame.init()
window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255,255,255))

while True:
    pygame.draw.circle( window,
                        pygame.Color(255,0,0),
                        (width/2, height/2),
                        radius, blank)
    pygame.display.update()

while True:
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
