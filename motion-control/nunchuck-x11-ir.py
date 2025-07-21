import subprocess
from evdev import InputDevice, ecodes
import sys

ir_device_path = '/dev/input/event17'
screen_width = 2560
screen_height = 1440

try:
    ir_dev = InputDevice(ir_device_path)
except FileNotFoundError:
    print(f"Device not found: {ir_device_path}")
    sys.exit(1)

print(f"Listening to: {ir_dev.name} ({ir_device_path})")

last_x, last_y = None, None

max_ir_x = 1023
max_ir_y = 1023

def move_mouse_absolute(x, y):
    subprocess.run(['xdotool', 'mousemove', str(2560-x), str(y)])

def handle_ir_events():
    global last_x, last_y
    for event in ir_dev.read_loop():
        if event.type == ecodes.EV_ABS:
            if event.code == ecodes.ABS_HAT0X:
                last_x = int(event.value * screen_width / max_ir_x)
            elif event.code == ecodes.ABS_HAT0Y:
                last_y = int(event.value * screen_height / max_ir_y)

            if last_x is not None and last_y is not None:
                print(f"Moving to: {last_x}, {last_y}")
                move_mouse_absolute(last_x, last_y)

handle_ir_events()
