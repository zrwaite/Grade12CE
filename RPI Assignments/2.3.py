#2.3
import gpiozero
from time import sleep

red = gpiozero.LED(17)
while(True):
    red.on()
    sleep(1)
    red.off()
    sleep(1)
