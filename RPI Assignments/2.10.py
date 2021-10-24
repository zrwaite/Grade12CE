#2.10
import gpiozero
from time import sleep
graph = gpiozero.LEDBarGraph(5, 6, 13, 19, 26, 20 pwm=True)
while True:
    graph.value = 1
    sleep(1)
    graph.value = 6/12
    sleep(1)
    graph.value = -6/12
    sleep(1)
    graph.value = 3/12
    sleep(1)
    graph.value = 8/12
    sleep(1)
