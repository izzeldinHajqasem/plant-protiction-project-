# Imports go at the top
from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
import radio 
initialize()
radio.config(group=5)
# Code in a 'while True:' loop repeats forever
while True:
    clear_oled()
    recive= radio.receive()
    if recive =="moisture level is low. pumping water " or recive == "a living organisim is near the plant":
        add_text(1,3,recive)
        sleep(20000)
    if button_a.is_pressed():
        radio.send("off")
    elif button_b.is_pressed():
        radio.send("on")

