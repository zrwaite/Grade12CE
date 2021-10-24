import gpiozero
from ADCDevice import *
from ADCDevice import PCF8591
from time import sleep

#5 input devices, adc is an array of 4 analog inputs, the others are digital
adc = PCF8591()
push1 = gpiozero.InputDevice(4)
push2 = gpiozero.InputDevice(17)
buttonL = gpiozero.InputDevice(22)
buttonR = gpiozero.InputDevice(27)

#11 output devices for assorted commands needed in minecraft
up = gpiozero.OutputDevice(26)
down = gpiozero.OutputDevice(19)
left = gpiozero.OutputDevice(13)
right = gpiozero.OutputDevice(6)
w = gpiozero.OutputDevice(7)
a = gpiozero.OutputDevice(8)
s = gpiozero.OutputDevice(25)
d = gpiozero.OutputDevice(24)
space = gpiozero.OutputDevice(23)
leftClick = gpiozero.OutputDevice(5)
rightClick = gpiozero.OutputDevice(21)

#These variables control the loop to allow for pre-made computer inputs
looping = False
loopCount = 0

#Program Loop
while(True):
    #Takes inputs and puts them into variables
    inputx1 = adc.analogRead(2)
    inputy1 = adc.analogRead(3)
    inputz1 = push1.value
    inputx2 = adc.analogRead(0)
    inputy2 = adc.analogRead(1)
    inputz2 = push2.value
    inputl = buttonL.value
    inputr = buttonR.value
    sleep(0.01)

    #Checks Button Inputs
    if inputl == 1:
        leftClick.off()
        print("Left Click")
    else:
        leftClick.on()
    if inputr == 1:
        rightClick.off()
        print("Right Click")
    else:
        rightClick.on()
    #Checks Left Joystick Inputs
    if inputx1 <=88:
        print("Left")
        left.off()
        right.on()
    elif inputx1 >= 168:
        print("Right")
        left.on()
        right.off()
    else:
        left.on()
        right.on()
    if inputy1 >= 168:
        print("Up")
        up.off()
        down.on()
    elif inputy1 <= 88:
        print("Down")
        up.on()
        down.off()
    else:
        up.on()
        down.on()
    if inputz1 == 0:
        print("Pushed")
        looping = True
    if looping:
        loopCount += 1
        if loopCount == 1:
            space.off()
        if loopCount == 5:
            space.on()
        if loopCount == 9:
            space.off()
        if loopCount == 13:
            space.on()
            looping = False
            loopCount = 0  
    #Checks Right Joystick Inputs
    if inputx2 <=88:
        print("a")
        a.off()
        d.on()
    elif inputx2 >=168:
        print("d")
        a.on()
        d.off()
    else:
        a.on()
        d.on()
    if inputy2 >= 168:
        print("w")
        w.off()
        s.on()
    elif inputy2 <= 88:
        print("s")
        w.on()
        s.off()
    else:
        w.on()
        s.on()
    if not looping:
        if inputz2 == 0:
            print("Other Pushed")
            space.off()
        else:
            space.on()
    
    


