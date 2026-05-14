from adafruit_circuitplayground import cp

#make a list to track past directions
#fixed yellow :D

end = 0
import random
import time
order = []
inputs = []
wait = 0
cp.pixels.fill((0, 0, 0))

def start():
    global wait
    order.append(random.randint(1, 4))
        
    for j in order:
                if j == 1:
                    for i in [0, 1]:
                        cp.pixels[i] = (0, 1, 0)
                    cp.play_tone(130.81, 0.5)
                    cp.pixels.fill((0, 0, 0))
        
                if j == 2:
                    for i in [2, 3, 4]:
                        cp.pixels[i] = (1, 1, 0)
                    cp.play_tone(146.83, 0.5)
                    cp.pixels.fill((0, 0, 0))
        
                if j == 3:
                    for i in [5, 6, 7]:
                        cp.pixels[i] = (0, 0, 1)
                    cp.play_tone(164.81, 0.5)
                    cp.pixels.fill((0, 0, 0))
        
                if j == 4:
                    for i in [8, 9]:
                        cp.pixels[i] = (1, 0, 0)
                    cp.play_tone(174.61, 0.5)
                    cp.pixels.fill((0, 0, 0))
                wait = 1

def your_turn():
    global wait
    global end
    while wait == 1:
        if cp.touch_A4:
            inputs.append(1)
            end = inputs.count(-1)
            if order[end] == inputs[-1]:
                for i in [0, 1]:
                    cp.pixels[i] = (0, 1, 0)
                cp.play_tone(130.81, 0.5)
                cp.pixels.fill((0, 0, 0))
                time.sleep(0.2)

            else:
                cp.pixels.fill((1, 0, 0))
                cp.play_tone(155.56, 0.5)
                cp.pixels.fill(0, 0, 0)
                order.clear()
                time.sleep(0.2)
    
        elif cp.touch_A7:
            inputs.append(2)
            end = inputs.count(-1)
            if order[end] == inputs[-1]:
                for i in [2, 3, 4]:
                    cp.pixels[i] = (1, 1, 0)
                cp.play_tone(146.83, 0.5)
                cp.pixels.fill((0, 0, 0))
                time.sleep(0.5)

            else:
                cp.pixels.fill((1, 0, 0))
                cp.play_tone(155.56, 0.5)
                cp.pixels.fill(0, 0, 0)
                order.clear()
                time.sleep(0.5)
    
        elif cp.touch_A0:
            inputs.append(3)
            end = inputs.count(-1)
            if order[end] == inputs[-1]:
                for i in [5, 6, 7]:
                    cp.pixels[i] = (0, 0, 1)
                cp.play_tone(164.81, 0.5)
                cp.pixels.fill((0, 0, 0))
                time.sleep(0.5)

            else:
                cp.pixels.fill((1, 0, 0))
                cp.play_tone(155.56, 0.5)
                cp.pixels.fill(0, 0, 0)
                order.clear()
                time.sleep(0.5)

        elif cp.touch_A3:
            inputs.append(4)
            end = inputs.count(-1)
            if order[end] == inputs[-1]:
                for i in [8, 9]:
                    cp.pixels[i] = (1, 0, 0)
                cp.play_tone(174.61, 0.5)
                cp.pixels.fill((0, 0, 0))
                time.sleep(0.5)

            else:
                cp.pixels.fill((1, 0, 0))
                cp.play_tone(155.56, 0.5)
                cp.pixels.fill(0, 0, 0)
                order.clear()
                time.sleep(0.5)        

        while len(order) == len(inputs):
            wait = 0
            inputs.clear
            


while True:
    if cp.button_a:
        if wait == 0:
                start()
        elif wait == 1:
                your_turn()

    