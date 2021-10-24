#2.4
import gpiozero
from time import sleep

red = gpiozero.PMWLED(17)
while(True):
    red.value = 0
    sleep(1)
    red.value = 0.5
    sleep(1)
    red.value = 1
    sleep(1)
