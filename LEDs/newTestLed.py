import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 8)

pixels[0] = (255,0,0)
pixels[1] = (255,255,0)
pixels[2] = (255,0,255)
pixels[3] = (255,255,255)
pixels[4] = (0,255,0)
pixels[5] = (0,0,255)
pixels[6] = (0,255,255)
pixels[7] = (0,0,255)
while True:
    pass