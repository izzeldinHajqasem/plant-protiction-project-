# Imports go at the top
from microbit import *
import radio
from ultrasonic import Ultrasonic

ultrasonic_sensor= Ultrasonic()
radio.config(group=5)
# Code in a 'while True:' loop repeats forever
while True:
    recive = radio.receive()
    moisture= pin0.read_analog()
    distance= ultrasonic_sensor.measure_distance_cm()
    if moisture <= 30:
        #code for the water bump  
        radio.send("moisture levels are low water is being droobing")
        if distance <=15:
            if recive == "off":
                sleep(50000)
            elif recive == "on":
                #buzzer to kick the animal
                pin2.write_digital(1)
                radio.send("a living organisim is near the plant")
                sleep(50000)
                pin2.write_digital(0)