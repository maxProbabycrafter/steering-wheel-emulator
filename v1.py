from mouse import get_position as mouse_get_pos
from pyvjoy import VJoyDevice, HID_USAGE_X, HID_USAGE_Z
from time import sleep

'''
--Steering wheel Emulator--

steering | Left-stick    | x-axis
throttle | Right-trigger | (+)z-axis
break    | Left-trigger  | (-)z-axis


'''
MAX_AXIS = 32768
device = VJoyDevice(1)
Steering = HID_USAGE_X
Throttle_Break = HID_USAGE_Z

def Main():
    while True:
        cordinates = mouse_get_pos()
        device.set_axis(Steering, cordinates[0] * 21)
        device.set_axis(Throttle_Break, cordinates[1] * 37)
        sleep(0.01)

def VjoyReset_input():
    device.set_axis(Steering, MAX_AXIS//2)
    device.set_axis(Throttle_Break, MAX_AXIS//2)
