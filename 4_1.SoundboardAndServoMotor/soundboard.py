import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

soundA = pygame.mixer.Sound("center.wav")
soundB = pygame.mixer.Sound("left.wav")
soundC = pygame.mixer.Sound("right.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Soundboard Ready."

while True:
    try:
        if (GPIO.input(24) == True):
            print("click")
            soundChannelA.play(soundB)
        sleep(1)
    except KeyboardInterrupt:
        exit()

