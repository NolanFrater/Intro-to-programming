from adafruit_circuitplayground import cp

cp.pixels.fill((0, 0, 0))

while True:
    x, y, z = cp.acceleration
    while cp.button_a:

        if x > 5: #right
            for i in [1, 2, 3, 4, 8, 9]:
                cp.pixels[i] = (1, 0, 0)
            

        if x < -5: #left
            for i in [1, 3, 5, 6]:
                cp.pixels[i] = (0, 1, 0)


        if y > 5: #forward
            for i in [3,5, 6, 7]:
                cp.pixels[i] = (1, 1, 0)

    
        if y < -5: #backward
            for i in [2, 4, 8]:
                cp.pixels[i] = (0, 0, 1)

        if x < 5 and x > -5 and y < 5 and y > -5:
            cp.pixels.fill((0, 0, 0))
                  