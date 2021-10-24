#2.8
import gpiozero
from time import sleep
from subprocess import check_call

def shutdown():
    check_call(["sudo", "poweroff"])
button = gpiozero.Button(2, hold_time=2)
while True:
    button.when_held = shutdown
    sleep(0.1)
