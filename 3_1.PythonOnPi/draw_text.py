import pygame

pygame.init()
screen = pygame.display.set_mode((752,92))
font = pygame.font.SysFont("freeserif", 72, bold = 1)
textSurface = font.render("No Pain, No Gain", 1, pygame.Color(255,255,255))
screen.blit(textSurface, (10,10))
while True:
    pygame.display.update()
