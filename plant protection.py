# Imports go at the top
from microbit import *
import radio


radio.config(group=5)
# Code in a 'while True:' loop repeats forever
while True:
    recive = radio.receive()
    moisture= pin0.read_analog()
    distance= pin2.read_digital()
    if moisture <= 500:
             pin16.write_digital(1)
             radio.send('moisture level is low. pumping water ')
             sleep(3000)
             pin16.write_digital(0)

    if distance <=15:
        if recive == "off":
            sleep(50000)
        else:
            #buzzer to kick the animal
            pin1.write_digital(1)
            radio.send("a living organisim is near the plant")
            sleep(50000)
            pin1.write_digital(0)
