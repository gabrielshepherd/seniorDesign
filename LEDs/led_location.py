# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
# Simple test for NeoPixels on Raspberry Pi
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
    pixel_pin, num_pixels, brightness=1.1, auto_write=False, pixel_order=ORDER
)
 
 
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
 
 
def rainbow_cycle(wait, j):
    # for j in range(255):
    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels) + j
        pixels[i] = wheel(pixel_index & 255)
    pixels.show()
    time.sleep(wait)

def snake():
    pixels.fill((0,0,0))
    pixels.show()
    for i in range(122):
        pixels[i] = (0,102,51)
        pixels.show()
    for j in range(460,565):
        pixels[j] = (0,102,51)
        pixels.show()
    for k in range(318,303,-1):
        pixels[k] = (0,102,51)
        pixels.show()
    for l in range(566,671):
        pixels[l] = (0,102,51)
        pixels.show()
    for m in range(137,152):
        pixels[m] = (0,102,51)
        pixels.show()
    for n in range(672,777):
        pixels[n] = (0,102,51)
        pixels.show()
    for p in range(289,274,-1):
        pixels[p] = (0,102,51)
        pixels.show()
    for q in range(274,168,-1):
        pixels[q] = (0,102,51)
        pixels.show()
    


        


def sectionA():
    pixels.fill(0,0,0)
    pixels.show()
    for k in range(0, 35):
        pixels[k] = COLOR      
        pixels.show()
   

def sectionB():
    pixels.fill(0,0,0)
    pixels.show()
    for k in range(37,72):
        pixels[k] = COLOR      
        pixels.show()
 

def sectionC():
    pixels.fill(0,0,0)
    pixels.show()
    for k in range(73, 109):
        pixels[k] = COLOR      
        pixels.show()
 

def sectionD():
    pixels.fill(0,0,0)
    pixels.show()
    for k in range(110, 122):
        pixels[k] = COLOR      
        pixels.show()


     
 
 
#while True:

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 0, 0))
    # sectionA()
    # sectionB()
    # sectionC()
    # sectionD()
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