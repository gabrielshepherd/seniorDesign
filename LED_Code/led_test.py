from gpiozero import LED
from time import sleep

led = LED(17)
while True:
    print("LED on")
    led.on()
    sleep(1)
    print("LED off")
    led.off()
    sleep(1)