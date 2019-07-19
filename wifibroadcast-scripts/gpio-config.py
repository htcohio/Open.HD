#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_state0 = GPIO.input(23)
input_state1 = GPIO.input(24)
input_state2 = GPIO.input(7)
nb = 1
if not input_state0:
    nb += 1
if not input_state1:
    nb += 2
if not input_state2:
    nb += 4
print( "openhd-settings-" + str(nb) + ".txt")


