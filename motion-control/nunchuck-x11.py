import subprocess
from evdev import InputDevice, ecodes
import sys

nunchuck_device_path = '/dev/input/event16'

DELTA_THRESHOLD = 1

try:
    nunchuck_dev = InputDevice(nunchuck_device_path)
except FileNotFoundError:
    print(f"Device not found: {nunchuck_device_path}")
    sys.exit(1)

print(f"Listening to: {nunchuck_dev.name} ({nunchuck_device_path})")

last_values_nunchuck = {}

def move_mouse_relative(dx, dy):
    subprocess.run(['xdotool', 'mousemove_relative', '--', str(dx), str(dy)])

def handle_nunchuck_events():
    for event in nunchuck_dev.read_loop():
        if event.type == ecodes.EV_ABS:
            code_name = ecodes.ABS.get(event.code, f"Unknown({event.code})")
            current_value_nunchuck = event.value

            last_value = last_values_nunchuck.get(event.code)
            if last_value is None:
                last_values_nunchuck[event.code] = current_value_nunchuck
                continue

            delta = current_value_nunchuck - last_value
            if abs(delta) >= DELTA_THRESHOLD:
                print(f"Nunchuck - {code_name}: {current_value_nunchuck} (Δ {delta})")
                last_values_nunchuck[event.code] = current_value_nunchuck

                if event.code == ecodes.ABS_RX:
                    move_mouse_relative(delta, 0)
                elif event.code == ecodes.ABS_RY:
                    move_mouse_relative(0, delta)

handle_nunchuck_events()
