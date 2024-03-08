import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio

keyboard = Keyboard(usb_hid.devices)
layout = Keycode(keyboard)

###### Edit "Button" to your designated button ######
button = layout.RIGHT_CTR
#####################################################

print("Initializing...")

#Get LED for morse visualtion
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

#Get input pins from the morseKey
input = digitalio.DigitalInOut(board.GP0)
input.direction = digitalio.Direction.INPUT
input.pull = digitalio.Pull.UP

led.value = False

morse = False

print("...Initialized sucessfully")

while True :

    if morse != input.value :
        morse = input.value
        if morse.value == True :
            keyboard.release(button)
            led.value = True
        elif morse.vale == False :
            keyboard.press(button)
            led.value = False

    time.sleep(0.01)
        






