#2.11
import gpiozero
from time import sleep
lights = gpiozero.TrafficLights(2, 3, 4)
while True:
    light.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(10)
    lights.green.on()
    lights.amber.off()
    lights.red.off()
    sleep(10)
