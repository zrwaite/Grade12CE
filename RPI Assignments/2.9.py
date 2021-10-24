#2.9
import gpiozero
from time import sleep

leds = gpiozero.LEDBoard(5, 6, 13, 19, 26, pwm=True)
while True:
    leds.on()
    sleep(1)
    leds(off)
    sleep(1)
    leds.value = (1, 0.75, 0.5, 0.75, 1)
    sleep(1)
    leds.blink()
    sleep(1)
