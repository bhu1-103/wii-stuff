from evdev import InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event16')

for event in dev.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.code == ecodes.ABS_RX:
            print(f"Accel X: {event.value//10}")
        elif event.code == ecodes.ABS_RY:
            print(f"Accel Y: {event.value//10}")
        elif event.code == ecodes.ABS_RZ:
            print(f"Accel Z: {event.value//10}")
