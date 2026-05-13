from adafruit_circuitplayground import cp

import time

while True:
    if cp.switch == True:
        for i in range(0, 5, 1):
            cp.pixels[i] = (0, 1, 0)
            for j in range(5, 10, 1):
                cp.pixels[j] = (0, 0, 0)
    
    if cp.switch == False:
        for k in range(5, 10, 1):
            cp.pixels[k] = (0, 1, 0)
            for l in range(0, 5, 1):
                cp.pixels[l] = (0, 0, 0)
   
            