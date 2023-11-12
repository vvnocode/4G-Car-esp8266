from machine import Pin

# ESP8266 ESP-12 modules have blue, active-low LED on GPIO2, replace
# with something else if needed.
led = Pin(2, Pin.OUT, value=1)

state = 0

def control_led(data):
    global state
    if data == "on":
        led.value(0)
        state = 1
    elif data == "off":
        led.value(1)
        state = 0
    elif data == "toggle":
        # LED is inversed, so setting it to current state
        # value will make it toggle
        led.value(state)
        state = 1 - state