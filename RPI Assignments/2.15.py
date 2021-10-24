#2.15
from time import sleep
from gpiozero import LED, Buzzer, Button

button = Button(2)
buzzer = Buzzer(3)
red = LED(4)
amber = LED(5)
green = LED(6)

things = [red, amber, green, buzzer]
def things_on():
        for thing in things:
            thing.on()

    def things_off():
        for thing in things:
            thing.off()
while True:
    button.when_pressed = things_on
    button.when_released = things_off
    sleep(0.01)
