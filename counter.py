from adafruit_circuitplayground import cp

import time
import random

cp.pixels.fill((0, 0, 0))
number = -1

while True:

    if number >= 0:
        cp.pixels[number] = (1, 0, 2)
    for i in range(number + 1, 10, 1):
        cp.pixels[i] = (0, 0, 0)
    
    

    if cp.button_a:
        number += 1
        time.sleep(0.2)
        if number >= 10:
            number = 9

    
    if cp.button_b:
        number -= 1
        time.sleep(0.2)
        if number <= -2:
            number = -1