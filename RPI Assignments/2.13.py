#2.13
import gpiozero
from time import sleep
from random import randint
led = gpiozero.LED(17)
p1 = gpiozero.Button(2)
p2 = gpiozero.Button(3)
winner = "none"
while True:
    led.on()
    delay = randint(0, 10)
    sleep(delay)
    while winner == "none":
        if p1.is_pressed:
            winner = "P1"
        elif p2.is_pressed:
            winner = "P2"
    if winner == "P1":
        print("Player 1 wins")
    elif winner == "P2":
        print("Player 2 wins")
    led.off()
    sleep(0.25)
    led.on()
    sleep(0.25)
    led.off()
    sleep(0.25)
    led.on()
    sleep(0.25)
    led.off()
    sleep(0.25)
    led.on()
    sleep(0.25)
    led.off()
