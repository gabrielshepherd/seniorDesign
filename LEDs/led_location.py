# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
 
CLEAR = (0, 0, 0)  # clear (or second color)

#Color as (R,G,B) - (0,102,51) is Bison green
COLOR = (0,255,0)

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 766
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

# Wheel function found online 
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

 
# Rainbow function for the idle mode
def rainbow_cycle(wait, j):
    # pixels.fill(wheel(j & 255))
    # pixels.show()
    # time.sleep(wait)

    for i in range(num_pixels):
        pixels[i] = wheel(j & 255)
    pixels.show()
    time.sleep(wait)
    # for i in range(335):
    #     pixel_index = (i * 256 // num_pixels) + j
    #     pixels[i] = wheel(pixel_index & 255)
    #     #pixels.fill(wheel(pixel_index & 255))
    # pixels.show()
    # time.sleep(wait)

#Broken snake function
def old_snake():
    pixels.fill((0,0,0))
    pixels.show()
    for i in range(122):
        pixels[i] = (0,51,102)
        pixels.show()
    for j in range(457,565):
        pixels[j] = (0,51,102)
        pixels.show()
    for k in range(318,303,-1):
        pixels[k] = (0,51,102)
        pixels.show()
    for l in range(566,671):
        pixels[l] = (0,51,102)
        pixels.show()
    for m in range(137,152):
        pixels[m] = (0,51,102)
        pixels.show()
    for n in range(672,777):
        pixels[n] = (0,51,102)
        pixels.show()
    for p in range(289,274,-1):
        pixels[p] = (0,51,102)
        pixels.show()
    for q in range(274,168,-1):
        pixels[q] = (0,51,102)
        pixels.show()

def snake(start):
    pixels[start] = COLOR
    pixels.show()
    time.sleep(0.001)

#Turns off all pixels 
def clear():
    pixels.fill(CLEAR)
    

# Dictionary of lists with the key being the location ID with its correspoding LED addresses.
codes = {
    'opamps': [(23, 35), (528, 541), (37, 49), (516, 528), (504, 516), (610, 623) ], #a13, b11, b22
    'diodes': [(468, 480), (647, 659), (457, 468), (659, 669), (122, 137) ], #c22, c23
    'voltreg': [(528, 541), (586, 598), (350, 365), (492, 504), (622, 635), (427, 442)],#a23, b23
    'ttl': [(0, 12), (553, 563), (319, 335),(11, 22), (542, 553), (553, 563), (563, 574), (304, 320)], #a11, a12, a21
    'transistors': [(49, 61), (504, 516), (61, 73), (492, 504), (73, 85), (480, 491), (622, 635), (635, 647)], #b12, b13, c11, b23, c21
    #'resistors': [(563, 574),(574, 586),(586, 598),(289, 304),(365,380),(274, 289),(262, 274), (250, 262), (238, 250), (599, 611), (258, 270), (610, 623), (246, 258), (692, 705), (221, 234), (412, 427)],
    'resistors': [(274, 304), (563, 598), (365, 380), (599, 623), (246, 274), (692, 705), (221, 234), (412, 427)],
    
    # The first pair of numbers is the top of the section. Second pair is the bottom. Third pair 
    # is the left or right side depending on if it's in section XX1 or XX3.
    'A11': [(0, 12), (553, 563),(319, 335)],
    'A12': [(11,22), (542, 553)],
    'A13': [(23, 35), (528, 541), (335, 350)],
    'A21': [(553, 563), (563, 574), (304,320)],
    'A22': [(541, 553), (574, 586)],
    'A23': [(528, 541), (586, 598), (350, 365)],
    'A31': [(563, 574), (765, 774), (289, 304)],
    'A32': [(574, 586), (753, 765)],
    'A33': [(586, 598), (741, 753), (365,380)],
    'A41': [(765, 774), (262, 274), (274, 289)],
    'A42': [(753, 765), (250, 262)],
    'A43': [(741, 753), (238, 250),(380,395)],

    'B11': [(37, 49), (516, 528), (335, 350)],
    'B12': [(49, 61), (504, 516)],
    'B13': [(61, 73), (492, 504), (445, 460)],
    'B21': [(516, 528), (599, 611), (350, 365)],
    'B22': [(504, 516), (610, 623)],
    'B23': [(492, 504), (622, 635), (430, 445)],
    'B31': [(599, 611), (728, 741), (365, 380)],
    'B32': [(610, 623), (716, 728)],
    'B33': [(622, 635), (704, 716), (412, 427)],
    'B41': [(599, 611), (258, 270), (380, 395)],
    'B42': [(610, 623), (246, 258)],
    'B43': [(622, 635), (233, 246), (395, 412)],

    'C11': [(73, 85), (480, 491), (445, 460)],
    'C12': [(85, 97), (468, 480)],
    'C13': [(97, 110), (457, 460), (110, 122)],
    'C21': [(480, 492), (635, 647), (427, 442)],
    'C22': [(468, 480), (647, 659)],
    'C23': [(457, 468), (659, 669), (121, 137)],
    'C31': [(635, 647), (692, 705), (412, 427)],
    'C32': [(647, 659), (681, 692)],
    'C33': [(659, 669), (669, 681), (137, 152)],
    'C41': [(692, 705), (221, 234), (412, 427)],
    'C42': [(610, 623), (246, 258)],
    'C43': [(622, 635), (233, 246), (395, 412)],
    
}

#Parses 'codes' to know which LEDs to light up.
def part_location(code):
    rangesForCode = codes[code]
    for pair in rangesForCode:
        start, end = pair
        for x in range(start, end):
            pixels[x] = COLOR
    pixels.show()


# Use below for debugging purposes
# while True:

part_location('resistors')
 
    #rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step