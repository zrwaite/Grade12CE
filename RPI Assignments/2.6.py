#2.6
import gpiozero
from time import sleep
button = gpiozero.Button(2)
red = LED(17)
while True:
    button.when_pressed = red.on
    button.when_released = red.off
    sleep(0.1)
