#LED's For Parts Inventory System
### Overview
We are using [WS_2812B RGB LED Strips](https://www.amazon.com/Programmable-Aclorol-Individually-Addressable-Raspberry/dp/B07BKNS7DJ/ref=sr_1_1?dchild=1&keywords=B07BKNS7DJ&qid=1618847458&sr=8-1). There are 6 strips connected in series on the shelf. The LED's are currently connected to GPIO18 (Pin 12) PWM on the Raspberry Pi. 
### Setup
The LED's need to be connected to a common ground with the Raspberry Pi. There also needs to be a minimum of 1000 Ohm resister between the data wire and the Raspberry Pi. The data wire needs to be connected to a PWM output using GPIOs 12, 18, 40, and 52. 
#### led_location.py
This file holds all of the functions to light up the LED's.  We are using an [Adafruit Industry library](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel) to change the color, brightness, and index of each LED. We also are using their [wheel function](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_rpi_simpletest.py) to create a rainbow effect of the LED's. Licence is found in the comments. You can find the installation for dependancy's at this webpage: https://circuitpython.readthedocs.io/projects/neopixel/en/latest/

#### led_animation.py
This file was found from [Raspberry Pi Tutorials, "Connect and Control WS2812 RGB LED Strips via Raspberry Pi."](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/). Used to explore different animations.

