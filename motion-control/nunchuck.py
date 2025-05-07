from evdev import InputDevice, ecodes
import sys

device_path = '/dev/input/event19'

DELTA_THRESHOLD = 10

try:
    dev = InputDevice(device_path)
except FileNotFoundError:
    print(f"Device not found: {device_path}")
    sys.exit(1)

print(f"Listening to: {dev.name} ({device_path})")

last_values = {}

for event in dev.read_loop():
    if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_RZ:
        code_name = ecodes.ABS[event.code]
        current_value = event.value

        last_value = last_values.get(event.code)
        if last_value is None:
            last_values[event.code] = current_value
            continue

        delta = current_value - last_value
        if abs(delta) >= DELTA_THRESHOLD:
            print(f"{code_name}: {current_value} (Δ {delta})")
            last_values[event.code] = current_value
