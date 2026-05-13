from adafruit_circuitplayground import cp

import time
import random

while True:
    if cp.button_a:
        cp.pixels.fill((0, 0, 0))
        number = random.randint(1, 10)
        for i in range(0, number, 1):
            cp.pixels[i] = (0, 2, 1)


    if cp.button_b:
        cp.pixels.fill((0, 0, 0))
