# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import random
import array
 
CLEAR = (0, 0, 0)  # clear (or second color)

#Color as (R,G,B) - (0,102,51) is Bison green
COLOR = (0,255,0)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 800
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)

# Wheel function found online 
# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_simpletest.py
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

# Clears all of the pixels
def clear():
    pixels.fill(CLEAR)
    pixels.show()

# Theater function found online
# https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips
def theater_mode():
    for j in range(70):
        for q in range(4):
            for i in range(0,332, 4):
                pixels[i+q] = wheel((i+j) & 255)
            pixels.show()
            time.sleep(0.05)
            for i in range(0, 332, 4):
                pixels[i+q] = (0,0,0)
    return

# list of tuples that contain the addresses to the LEDs for the 12 boxes
boxes = {
    1: [(0,35),(528,563),(319,335),(335,350)],
    2: [(528,563),(563,598),(305,320),(350,365)],
    3: [(563,598),(741,775),(289,304),(365,380)],
    4: [(741,775),(238,274),(274,289),(380,395)],
    5: [(37,73),(492,528),(335,350),(442,457)],
    6: [(492,528),(599,635),(350,365),(427,442)],
    7: [(599,635),(704,741),(365,380),(412,427)],
    8: [(704,741),(201,238),(380,396),(396,412)],
    9: [(73,110),(457,491),(442,457),(110,122)],
    10: [(457,492),(635,669),(427,442),(121,137)],
    11: [(635,669),(669,705),(412,427),(137,152)],
    12: [(669,705),(165,201),(396,412),(152,165)],
}

# Function picks a color and changes intensity
def colors(color, index):
    if color == 1:                  #red
        return (index,0,0)
    if color == 2 :                 #green   
        return (0,index,0)
    if color == 3:                  #blue
        return (0,0,index)
    if color == 4:                  #yellow
        return (index,index,0)
    if color == 5 :                 #purple   
        return (index,0,index)
    if color == 6:                  #aqua
        return (0,index,index)
    if color == 7:                  #white
        return (index,index,index)

# Lights up a random box and with a brighter then dimmer transition
def random_box():
    # Cycle 10 times
    for number_of_cycles in range(10):
        number = random.randint(1,12)
        new_color = random.randint(1,7)
        rangesForCode = boxes[number]
        #Increase color intensity to 70 out of 255
        for brighter in range(70):
            #Parse the tuples
            for pair in rangesForCode:
                start, end = pair
                for x in range(start,end):
                    pixels[x] = colors(new_color, brighter)       
            pixels.show()
            time.sleep(0.005)
        #Decrease color intensity
        for dimmer in range(70,-1,-1):
            #Parse the tuples
            for pair in rangesForCode:
                start, end = pair
                for x in range(start,end):
                    pixels[x] = colors(new_color, dimmer)
            pixels.show()
            time.sleep(0.005)
    return

# List of tuples for the vertical_snake function.
snake = [(0,35,1),(335,395,1),(237,201,-1),(396,457,1),(73,335,1)]

# Snake runs vertically with a width of 8 LEDs
def vertical_snake():
    # Run 5 times. New snake color each time
    for i in range(5):
        new_color = random.randint(1,7)
        light = 0                       # keeps track of where the head is at the beginning
        light2 = 0                      # keeps track of where the head is after first transition
        light3 = 0                      # 
        light4 = 210
        light5 = 448
        light6 = 73
        light7 = 327

        #Parse snake tuple
        for tup in snake:
            start, end, increment = tup
            for x in range(start, end, increment):
                # This if statement is never called. 
                if light >= 462:
                    pixels[x - 8] = (0,0,0)
                else:
                    pixels[x] = colors(new_color, 255)
                light +=1
                light2 = light + 300
                light3 = light + 142
                if light <= 8:
                    pixels[335+x - 8] = (0,0,0)
                
                #First section
                if light >= 8 and light < 35:
                    
                    pixels[light - 8] = (0,0,0)
                #Transistion
                if light >= 35 and light < 43: 
                    pixels[light - 8] = (0,0,0)
                    pixels[light2 - 8] = (0,0,0)
                #Second section
                if light >= 43 and light < 95:
                    pixels[light2 - 8] = (0,0,0)
                #Transistion
                if light >=95 and light < 103:
                    pixels[light2 - 8] = (0,0,0)
                    pixels[light3 +8] = (0,0,0)
                #Bottom Section
                if light >= 103 and light < 131:
                    pixels[x +8] = (0,0,0)
                #Transistion
                if light >= 131 and light < 140:
                    pixels[light4] = (0,0,0)
                    light4 -= 1
                #Section going up
                if light >= 139 and light < 192:
                    pixels[x-8] = (0,0,0)
                #Transistion
                if light >= 192 and light < 208:
                    pixels[light5] = (0,0,0)
                    light5 += 1
                if light >= 192 and light < 462:
                    pixels[x-8] = (0,0,0)
                    light6 += 1
                    
                pixels.show()
    clear()
    return

# Picks a random LEDs to light up
def bouncing_led():
    clear()
    randomColor = random.randint(1,7)
    for i in range(500):
        randomLED = random.randint(1,780)
        pixels[randomLED] = colors(randomColor, 255)
        pixels.show()
        time.sleep(0.01)
    clear()

# Betting game which selects a random box with a roulette wheel transition
def roulette_wheel():
    randomColor = random.randint(1,7)
    wait = 0.1
    # Bounce between boxes 20 times
    for i in range(20):
        randomNumber = random.randint(1,12)
        randomBox = boxes[randomNumber] 
        # Parse boxes tuples
        for pair in randomBox:
            start, end = pair
            for x in range(start,end):
                pixels[x] = colors(randomColor, 255)
        pixels.show()
        #Slowly increase the wait to slow down the transistions
        wait *= 1.13
        time.sleep(wait)
        if i < 19:
            pixels.fill((0,0,0))
            pixels.show()

    # Winning box flashes 5 times
    for flash in range(5):
        clear()
        time.sleep(0.1)
        for pair in randomBox:
            start, end = pair
            for x in range(start,end):
                pixels[x] = colors(randomColor, 255)
        pixels.show()
    
    
        





        