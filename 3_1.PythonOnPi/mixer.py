import pygame.mixer
from time import sleep

pygame.mixer.init(48000, -16, 1, 1024)

sound = pygame.mixer.Sound("/home/pi/python_games/match5.wav")

channel1A = pygame.mixer.Channel(1)
channel1A.play(sound)

sleep(2.0)
