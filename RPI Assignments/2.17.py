#2.17
from time import sleep
from gpiozero import MotionSensor, LED

led = LED(16)
sensor = MotionSensor(4)

while True:
    sensor.when_motion = led.on
    sensor.when_no_motion = led.off
    sleep(0.01)
        
    
