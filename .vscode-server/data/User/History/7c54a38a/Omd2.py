import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin,1)
    time.sleep(0.5)
    