from machine import Pin
import time

# Pin: P14 for Pysense board
# Pin: G17 for Extension board

is_pressed = False
def handler(pin):
    global is_pressed
    value = pin.value()
    if not value and not is_pressed:
        print('Button pressed')
        is_pressed = True
    elif value and is_pressed:
        print('Button released')
        is_pressed = False
    else:
        pass

btn = Pin("P14", mode=Pin.IN, pull=Pin.PULL_UP)
btn.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, handler)
