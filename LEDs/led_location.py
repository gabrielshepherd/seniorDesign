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
num_pixels = 800
 
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

    # All LED's will be the same color
    for i in range(num_pixels):
        pixels[i] = wheel(j & 255)
    pixels.show()
    time.sleep(wait)

    # Each LED is a different color
    # for i in range(335):
    #     pixel_index = (i * 256 // num_pixels) + j
    #     pixels[i] = wheel(pixel_index & 255)
    #     #pixels.fill(wheel(pixel_index & 255))
    # pixels.show()
    # time.sleep(wait)


def snake(start, color):
    if color == 'yellow':
        pixels[start] = (255,255,0) #Yellow
    if color == 'green':
        pixels[start] = (0,255,0) #Green
    pixels.show()
    time.sleep(0.001)

def rainbow_snake(start, color):
    pixels[start] = wheel(color & 255 )
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
    'resistors': [(274, 304), (563, 598), (365, 380), (716,740), (214, 271),(692, 705), (189, 201), (396, 412)],
    'bulk': [(728, 741), (226, 238), (380, 396),(716, 728), (214, 226),(692, 705), (189, 201), (396, 412)],
    'quarterwatt': [(289, 304),(741,775),(563,598),(365,380)],
    'capacitors':[(610,648),(692,729)],
    'inductors':[(647, 659), (681, 692),(659, 669), (669, 681), (137, 152)],
    
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
    'B13': [(61, 73), (492, 504), (442, 457)],
    'B21': [(516, 528), (599, 611), (350, 365)],
    'B22': [(504, 516), (610, 623)],
    'B23': [(492, 504), (622, 635), (427, 442)],
    'B31': [(599, 611), (728, 741), (365, 380)],
    'B32': [(610, 623), (716, 728)],
    'B33': [(622, 635), (704, 716), (412, 427)],
    'B41': [(728, 741), (226, 238), (380, 396)],
    'B42': [(716, 728), (214, 226)],
    'B43': [(704, 716), (201, 214), (396, 412)],

    'C11': [(73, 85), (480, 491), (442, 457)],
    'C12': [(85, 97), (468, 480)],
    'C13': [(97, 110), (457, 468), (110, 122)],
    'C21': [(480, 492), (635, 647), (427, 442)],
    'C22': [(468, 480), (647, 659)],
    'C23': [(457, 468), (659, 669), (121, 137)],
    'C31': [(635, 647), (692, 705), (412, 427)],
    'C32': [(647, 659), (681, 692)],
    'C33': [(659, 669), (669, 681), (137, 152)],
    'C41': [(692, 705), (189, 201), (396, 412)],
    'C42': [(681, 692), (177, 189)],
    'C43': [(669, 681), (165, 177), (152,165)],
    
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
#while True:

#     part_location('A11')
#     time.sleep(1)
#     clear()
#     part_location('A12')
#     time.sleep(1)
#     clear()
#     part_location('A13')
#     time.sleep(1)
#     clear()
#     part_location('A21')
#     time.sleep(1)
#     clear()
#     part_location('A22')
#     time.sleep(1)
#     clear()
#     part_location('A23')
#     time.sleep(1)
#     clear()

#     part_location('A31')
#     time.sleep(1)
#     clear()
#     part_location('A32')
#     time.sleep(1)
#     clear()
#     part_location('A33')
#     time.sleep(1)
#     clear()

#     part_location('A41')
#     time.sleep(1)
#     clear()
#     part_location('A42')
#     time.sleep(1)
#     clear()
#     part_location('A43')
#     time.sleep(1)
#     clear()

    # part_location('B11')
    # time.sleep(1)
    # clear()
    # part_location('B12')
    # time.sleep(1)
    # clear()
    # part_location('B13')
    # time.sleep(1)
    # clear()

    # part_location('B21')
    # time.sleep(1)
    # clear()
    # part_location('B22')
    # time.sleep(1)
    # clear()
    # part_location('B23')
    # time.sleep(1)
    # clear()

    # part_location('B31')
    # time.sleep(1)
    # clear()
    # part_location('B32')
    # time.sleep(1)
    # clear()
    # part_location('B33')
    # time.sleep(1)
    # clear()

    # part_location('B41')
    # time.sleep(1)
    # clear()
    # part_location('B42')
    # time.sleep(1)
    # clear()
    # part_location('B43')
    # time.sleep(1)
    # clear()

    # part_location('C11')
    # time.sleep(1)
    # clear()
    # part_location('C12')
    # time.sleep(1)
    # clear()
    # part_location('C13')
    # time.sleep(1)
    # clear()

    # part_location('C21')
    # time.sleep(1)
    # clear()
    # part_location('C22')
    # time.sleep(1)
    # clear()
    # part_location('C23')
    # time.sleep(1)
    # clear()

    # part_location('C31')
    # time.sleep(1)
    # clear()
    # part_location('C32')
    # time.sleep(1)
    # clear()
    # part_location('C33')
    # time.sleep(1)
    # clear()

    # part_location('C41')
    # time.sleep(1)
    # clear()
    # part_location('C42')
    # time.sleep(1)
    # clear()
    # part_location('C43')
    # time.sleep(1)
    # clear()
 
    #rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step