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

def clear():
    pixels.fill(CLEAR)
    pixels.show()

def theater_mode():
    for j in range(70):
        for q in range(4):
            for i in range(0,333, 4):
                pixels[i+q] = wheel((i+j) & 255)
            pixels.show()
            time.sleep(0.05)
            for i in range(0, 333, 4):
                pixels[i+q] = (0,0,0)
boxes = {
    1: [(0,35),(528,563),(319,335),(335,350)],
    2: [(528,563),(563,598),(305,320),(350,365)],
    3: [(563,598),(741,774),(289,304),(365,380)],
    4: [(741,774),(238,274),(274,289),(380,395)],
    5: [(37,73),(492,528),(335,350),(442,457)],
    6: [(492,528),(599,635),(350,365),(427,442)],
    7: [(599,635),(704,741),(365,380),(412,427)],
    8: [(704,741),(201,238),(380,396),(396,412)],
    9: [(73,110),(457,491),(442,457),(110,122)],
    10: [(457,492),(635,669),(427,442),(121,137)],
    11: [(635,669),(669,705),(412,427),(137,152)],
    12: [(669,705),(165,201),(396,412),(152,165)],
}
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return r,g,b

def random_box():
    level = 100
    for number_of_cycles in range(12):
        number = random.randint(1,12)
        rangesForCode = boxes[number]
        randColor = random_color()
        
        for brighter in range(99):
            level -= 1
            for pair in rangesForCode:
                start, end = pair
                for x in range(start,end):
                    pixels[x] = (randColor[0] // level, randColor[1] // level, randColor[2] // level)
            pixels.show()
            time.sleep(0.005)

        for dimmer in range(99):
            level += 1
            for pair in rangesForCode:
                start, end = pair
                for x in range(start,end):
                    pixels[x] = (randColor[0] // level, randColor[1] // level, randColor[2] // level)
            pixels.show()
            time.sleep(0.005)

        
random_box()