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

def clear():
    pixels.fill(CLEAR)
    pixels.show()

def theater_mode():
    for j in range(10):
        for q in range(3):
            for i in range(0, num_pixels, 3):
                pixels[i] = wheel(i & 255)
            pixels.show()
            time.sleep(0.05)
            for i in range(0, num_pixels, 3):
                pixels[i] = wheel(i & 255)
# boxes = {
#     1: [()],
#     2: [()],
#     3: [()],
#     4: [()],
#     5: [()],
#     6: [()],
#     7: [()],
#     8: [()],
#     9: [()],
#     10: [()],
#     11: [()],
#     12: [()],

# }


# def random_box():
clear()
theater_mode()
#     theater_mode()
