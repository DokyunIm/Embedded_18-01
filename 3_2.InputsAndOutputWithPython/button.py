import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

count = 0

while True:
    inputValue = GPIO.input(23)
    if(inputValue == True):
        count = count +1
        print("Button pressed" + str(count) + "times.")
    time.sleep(.3)
