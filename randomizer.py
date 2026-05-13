from adafruit_circuitplayground import cp

import time
import random
shake_threshold = 15.0

while True:
    x, y, z = cp.acceleration
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:

        for i in range(0, 10, 1):
            cp.pixels[i] = (random.randint(0, 32), random.randint(0, 32), random.randint(0, 32))