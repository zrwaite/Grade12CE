#2.5
import gpiozero
from time import sleep
button = gpiozero.Button(2)

def hi():
    print("Good day to you fine sir")
def hi():
    print("I bid you aideu until we meet again")
def ifPressed():
    print("If Pressed:")
    i = 0
    while i<40:
        if button.is_pressed:
            print("Button is pressed")
            i+=1
        else:
            print("Button is not pressed")
        sleep(0.1)
def untilPress():
    print("Until Press:")
    button.wait_for_press()
    print("Button was pressed")

def whenPressed():
    i = 0
    while i<3:
        button.when_pressed = hi
        button.when_released = bye
        i+=1
        sleep(0.1)
