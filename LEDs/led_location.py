# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
 
CLEAR = (0, 0, 0)  # clear (or second color)
COLOR = (0,255,255)
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 900
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
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
    # for j in range(255):
    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels) + j
        pixels[i] = wheel(pixel_index & 255)
    pixels.show()
    time.sleep(wait)

#Broken snake function
def snake():
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

#Turns off all pixels 
def clear():
    pixels.fill(CLEAR)

#Dictionary of each section location
def part_location(location):

    if location == 'A11':
        sectionA11()
    if location == 'A12':
        sectionA12()
    if location == 'A13':
        sectionA13()

    # switcher = {
    #     'A11': sectionA11,
    #     'A12': sectionA12,
    #     'A13': sectionA13,
        # 'A21': sectionA21,
        # 'A22': sectionA22,
        # 'A23': sectionA23,
        # 'a31': sectionA31,
        # 'a32': sectionA32,
        # 'a33': sectionA33,
        # 'a41': sectionA41,
        # 'a42': sectionA42,
        # 'a43': sectionA43,
        # 'b11': sectionB11,
        # 'b12': sectionB12,
        # 'b13': sectionB13,
        # 'b21': sectionB21,
        # 'b22': sectionB22,
        # 'b23': sectionB23,
        # 'b31': sectionB31,
        # 'b32': sectionB32,
        # 'b33': sectionB33,
        # 'b41': sectionB41,
        # 'b42': sectionB42,
        # 'b43': sectionB43,
        # 'c11': sectionC11,
        # 'c12': sectionC12,
        # 'c13': sectionC13,
        # 'c21': sectionC21,
        # 'c22': sectionC22,
        # 'c23': sectionC23,
        # 'c31': sectionC31,
        # 'c32': sectionC32,
        # 'c33': sectionC33,
        # 'c41': sectionC41,
        # 'c42': sectionC42,
        # 'c43': sectionC43,
    #}
    return 
    # switcher.get(location,clear)



def sectionA11():
    for k in range(0, 12):
        pixels[k] = COLOR 
    for j in range(553, 563):
        pixels[j] = COLOR  
    for i in range(319, 335):
        pixels[i] = COLOR      
    pixels.show()

def sectionA12():
    for k in range(11, 22):
        pixels[k] = COLOR
    for j in range(542, 553):
        pixels[j] = COLOR       
    pixels.show()

def sectionA13():
    for k in range(23, 35):
        pixels[k] = COLOR
    for j in range(528, 541):
        pixels[j] = COLOR
    for i in range(335, 350):
        pixels[i] = COLOR       
    pixels.show()

def sectionA21():
    for k in range(553, 563):
        pixels[k] = COLOR 
    for j in range(563, 574):
        pixels[j] = COLOR
    for i in range(304, 320):
        pixels[i] = COLOR     
    pixels.show()

def sectionA22():
    for k in range(541, 553):
        pixels[k] = COLOR 
    for j in range(574, 586):
        pixels[j] = COLOR     
    pixels.show()

def sectionA23():
    for k in range(528, 541):
        pixels[k] = COLOR   
    for j in range(586, 598):
        pixels[j] = COLOR 
    for i in range(350, 365):
        pixels[i] = COLOR     
    pixels.show()   
    pixels.show()

def sectionA31():
    for k in range(563, 574):
        pixels[k] = COLOR 
    for j in range(765, 774):
        pixels[j] = COLOR
    for i in range(289, 304):
        pixels[i] = COLOR     
    pixels.show()

def sectionA32():
    for k in range(574, 586):
        pixels[k] = COLOR 
    for j in range(753, 765):
        pixels[j] = COLOR     
    pixels.show()

def sectionA33():
    for k in range(586, 598):
        pixels[k] = COLOR   
    for j in range(741, 753):
        pixels[j] = COLOR
    for i in range(365, 380):
        pixels[i] = COLOR      
    pixels.show()   
    pixels.show()

def sectionA41():
    for k in range(765, 774):
        pixels[k] = COLOR 
    for j in range(262, 274):
        pixels[j] = COLOR 
    for i in range(274, 289):
        pixels[i] = COLOR    
    pixels.show()

def sectionA42():
    for k in range(753, 765):
        pixels[k] = COLOR 
    for j in range(250, 262):
        pixels[j] = COLOR     
    pixels.show()

def sectionA43():
    for k in range(741, 753):
        pixels[k] = COLOR   
    for j in range(238, 250):
        pixels[j] = COLOR 
    for i in range(380, 395):
        pixels[i] = COLOR     
    pixels.show()   
    pixels.show()

# def sectionA31():
#     #pixels.fill((0,0,0))
    
#     for k in range(0, 109):
#         pixels[k] = COLOR      
#     pixels.show()

# def sectionA32():
#     #pixels.fill((0,0,0))
    
#     for k in range(0, 109):
#         pixels[k] = COLOR      
#     pixels.show()


# def sectionA33():
#     #pixels.fill((0,0,0))
    
#     for k in range(0, 109):
#         pixels[k] = COLOR      
#     pixels.show()
   
# def sectionA41():
#     #pixels.fill((0,0,0))
    
#     for k in range(0, 109):
#         pixels[k] = COLOR      
#     pixels.show()

# def sectionA42():
#     #pixels.fill((0,0,0))
   
#     for k in range(0, 109):
#         pixels[k] = COLOR      
#     pixels.show()

# def sectionA43():
#     #pixels.fill((0,0,0))
    
#     for k in range(0, 109):
#         pixels[k] = COLOR      
#     pixels.show()





 

# def sectionC():
#     #pixels.fill((0,0,0))
#     pixels.show()
#     for k in range(566, 671):
#         pixels[k] = COLOR      
#         pixels.show()
 

# def sectionD():
#     #pixels.fill((0,0,0))
#     pixels.show()
#     for k in range(169, 274):
#         pixels[k] = COLOR      
#         pixels.show()


     
 
 
while True:
#     # Comment this line out if you have RGBW/GRBW NeoPixels
    sectionA31()
    time.sleep(5)
    pixels.fill((0, 0, 0))
    sectionA32()
    time.sleep(5)
    pixels.fill((0, 0, 0))
    sectionA33()
    time.sleep(5)
    pixels.fill((0, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(5)


    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((255, 0, 0, 0))
    # pixels.show()
    # time.sleep(1)
 
    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((0, 255, 0, 0))
    # pixels.show()
    # time.sleep(1)
 
    # # Comment this line out if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((0, 0, 255, 0))
    # pixels.show()
    # time.sleep(1)


    # pixels.fill(CLEAR)
    # pixels.show()


  
 
    #rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step