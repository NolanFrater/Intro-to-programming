from adafruit_circuitplayground import cp

import time

cp.pixels.fill((0, 0, 0))

while True:
    if cp.light > 30:
        cp.pixels.fill((0, 0, 0))

    if cp.light <= 30:
        cp.pixels[0] = (1, 1, 1)
    
    if cp.light <= 27:
        cp.pixels[1] = (1, 1, 1)
    
    if cp.light <= 24:
        cp.pixels[2] = (1, 1, 1)

    if cp.light <= 21:
        cp.pixels[3] = (1, 1, 1)
    
    if cp.light <= 18:
        cp.pixels[4] = (1, 1, 1)
    
    if cp.light <= 15:
        cp.pixels[5] = (1, 1, 1)

    if cp.light <= 12:
        cp.pixels[6] = (1, 1, 1)
    
    if cp.light <= 9:
        cp.pixels[7] = (1, 1, 1)

    if cp.light <= 6:
        cp.pixels[8] = (1, 1, 1)

    if cp.light <= 3:
        cp.pixels[9] = (1, 1, 1)
                
            