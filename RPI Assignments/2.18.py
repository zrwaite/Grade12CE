#2.18
from time import sleep
from gpiozero import LightSensor, PWMLED

led = PWMLED(16)
sensor = LightSensor(18)

while True:
    is sensor.value >= 0 and sensor.value <= 1:
         led.value = 1-sensor.value
    else:
        print(sensor.value)
        
    
