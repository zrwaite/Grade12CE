#2.16
from time import sleep
from gpiozero import RGBLED

led = RGBLED(red=9, green=10, blue=11)

while True:
    led.color(0, 1, 0)
    sleep(1)
    led.color(1, 0, 1)
    sleep(1)
    led.color(1, 1, 1)
    sleep(1)
    for i in range(10):
        led.green= 1-(i/10)
        sleep(0.1)
    for i in range(10):
        led.red= 1-(i/10)
        sleep(0.1)
    for i in range(10):
        led.blue= 1-(i/10)
        sleep(0.1)
        
    
