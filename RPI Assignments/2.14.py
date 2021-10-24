#2.14
import gpiozero
import pygame.mixer
from pygame.mixer import Sound
from time import sleep

pygame.mixer.init()

button_sounds = {
    gpiozero.Button(2): Sound("samples/drum_tom_mid_hard.wav"),
    gpiozero.Button(3): Sound("samples/drum_cymbal_open.wav"),
}

while True:
    for button, sound in button_sounds.items():
        button.when_pressed = sound.play
    sleep(1)
