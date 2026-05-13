from adafruit_circuitplayground import cp

import time

cp.pixels.fill((252, 0, 0)) #all red

order = 1

while True:
    cp.pixels.brightness = 0.1
    if cp.button_a:
        order += 1
        time.sleep(0.2)
    
    if order >= 8:
        order = 1
    
    if order == 1:
        cp.pixels.fill((252, 0, 0)) #red

    if order == 2:
        cp.pixels.fill((201, 50, 0)) #orange
    
    if order == 3:
        cp.pixels.fill((201, 97, 0)) #yellow
    
    if order == 4:
        cp.pixels.fill((14, 99, 11)) #green
                
    if order == 5:
        cp.pixels.fill((48, 35, 222)) #blue

    if order == 6:
        cp.pixels.fill((146, 29, 196)) #purplple     

    if order == 7:
        cp.pixels.fill((252, 3, 28)) #Pink     