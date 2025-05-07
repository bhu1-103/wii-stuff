import subprocess
from evdev import InputDevice, ecodes
import sys

# Device path for Nunchuck
nunchuck_device_path = '/dev/input/event19'  # Replace with your actual Nunchuck device path

# Threshold for delta change
DELTA_THRESHOLD = 10

# Try to open the Nunchuck input device
try:
    nunchuck_dev = InputDevice(nunchuck_device_path)
except FileNotFoundError:
    print(f"Device not found: {nunchuck_device_path}")
    sys.exit(1)

print(f"Listening to: {nunchuck_dev.name} ({nunchuck_device_path})")

# Store last values for delta calculations
last_values_nunchuck = {}

# Function to move the mouse relatively using ydotool
def move_mouse_relative(dx, dy):
    #subprocess.run(['ydotool', 'mousemove', str(dx), str(dy)])
    subprocess.run(['ydotool', 'mousemove', '-x', str(dx), '-y', str(dy)])

# Function to handle events and control the mouse
def handle_nunchuck_events():
    for event in nunchuck_dev.read_loop():
        if event.type == ecodes.EV_ABS:
            code_name = ecodes.ABS.get(event.code, f"Unknown({event.code})")
            current_value_nunchuck = event.value

            # Delta calculation
            last_value = last_values_nunchuck.get(event.code)
            if last_value is None:
                last_values_nunchuck[event.code] = current_value_nunchuck
                continue

            delta = current_value_nunchuck - last_value
            if abs(delta) >= DELTA_THRESHOLD:
                print(f"Nunchuck - {code_name}: {current_value_nunchuck} (Δ {delta})")
                last_values_nunchuck[event.code] = current_value_nunchuck

                # Move the mouse relative based on the accelerometer data
                if event.code == ecodes.ABS_RX:
                    move_mouse_relative(delta*3, 0)  # Move on X-axis (relative)
                elif event.code == ecodes.ABS_RY:
                    move_mouse_relative(0, delta*3)  # Move on Y-axis (relative)

handle_nunchuck_events()
