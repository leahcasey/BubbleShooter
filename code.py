from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from sensordisplay import *
import usb_hid

kbd = Keyboard(usb_hid.devices)

sld = SensorLightDisplay(0.1)

acceleration_peak = 9.81

black = [0, 0, 0]

while True:

    if cp.switch:
        x = cp.acceleration[0]

        sld.advanced_control_feedback(x)
        if x <= acceleration_peak and x > -9.81:

            if x > 3:
                kbd.press(Keycode.RIGHT_ARROW)

                if cp.button_a or cp.button_b:
                    kbd.send(Keycode.SPACEBAR)

            elif x < -3:
                kbd.press(Keycode.LEFT_ARROW)

                if cp.button_a or cp.button_b:
                    kbd.send(Keycode.SPACEBAR)

            elif cp.button_a or cp.button_b:
                kbd.send(Keycode.SPACEBAR)

            else:
                kbd.release(Keycode.LEFT_ARROW)
                kbd.release(Keycode.RIGHT_ARROW)

        else:
            kbd.release(Keycode.LEFT_ARROW)
            kbd.release(Keycode.RIGHT_ARROW)

    else:
        kbd.release(Keycode.LEFT_ARROW)
        kbd.release(Keycode.RIGHT_ARROW)
        cp.pixels.fill(black)
        cp.pixels.show()
