from mouse import get_position as mouse_get_pos
from pyvjoy import VJoyDevice, HID_USAGE_X, HID_USAGE_Z, HID_USAGE_Y, HID_USAGE_RX, HID_USAGE_RY, HID_USAGE_RZ
from time import sleep

'''
--Steering wheel Emulator--

steering | Left-stick    | x-axis
throttle | Right-trigger | (+)z-axis
break    | Left-trigger  | (-)z-axis


'''
MAX_AXIS = 32768
HALF_AXIS = 32768 // 2
device = VJoyDevice(1)
Steering = [HID_USAGE_X, HID_USAGE_Y]
Throttle_Break = HID_USAGE_Z

def Main(MouseRange):

    device.set_axis(Steering[1], HALF_AXIS)
    device.set_axis(HID_USAGE_RX, HALF_AXIS)
    device.set_axis(HID_USAGE_RY, HALF_AXIS)
    device.set_axis(HID_USAGE_RZ, HALF_AXIS)
    
    while True:
        cordinates = mouse_get_pos()
        device.set_axis(Steering[0], cordinates[0] * MAX_AXIS // MouseRange[0])
        device.set_axis(Throttle_Break, cordinates[1] * MAX_AXIS // MouseRange[1])
        sleep(0.01)

def VjoyReset_input():
    device.set_axis(Steering[0], HALF_AXIS)
    device.set_axis(Throttle_Break, HALF_AXIS)
