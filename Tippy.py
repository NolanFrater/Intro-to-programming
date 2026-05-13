from adafruit_circuitplayground import cp

import time

while True:
    x, y, z = cp.acceleration

    if x < -5:
        for i in range(6, 9, 1):
            cp.pixels[i] = (1, 0, 0)
            for j in range(1, 4, 1):
                cp.pixels[j] = (0, 0, 0)

    elif x > 5:
        for k in range(1, 4, 1):
            cp.pixels[k] = (0, 1, 0)
            for j in range(6, 9, 1):
                cp.pixels[j] = (0, 0, 0)
    