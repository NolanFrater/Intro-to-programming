from adafruit_circuitplayground import cp

import time

cp.pixels.fill((0, 0, 0))

order = 0

while True:
    if order == 9:
        cp.pixels.fill((0, 1, 0))
        cp.play_tone(800, 0.5)
        cp.pixels.fill((0, 0, 0))
        order = 0

    if cp.button_a:
        order += 1
        if order == 1 or 2 or 4 or 8:
            cp.pixels.fill((0, 0, 1))
            time.sleep(0.5)
            cp.pixels.fill((0, 0, 0))
        else:
            cp.pixels.fill((1, 0, 0))
            cp.play_tone(500, 0.5)
            cp.pixels.fill((0, 0, 0))
            order = 0
    
    if cp.button_b:
        order += 1
        if order == 3 or 5 or 6 or 7:
            cp.pixels.fill((0, 0, 1))
            time.sleep(0.5)
            cp.pixels.fill((0, 0, 0))
        else:
            cp.pixels.fill((1, 0, 0))
            cp.play_tone(500, 0.5)
            cp.pixels.fill((0, 0, 0))
            order = 0
    
    if cp.button_a and cp.button_b:
        order += 1
        if order == 9:
            time.sleep(0.5)
        else:
            cp.pixels.fill((1, 0, 0))
            cp.play_tone(500, 0.5)
            cp.pixels.fill((0, 0, 0))
            order = 0