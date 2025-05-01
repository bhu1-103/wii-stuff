from evdev import InputDevice, ecodes

dev = InputDevice('/dev/input/event18')

code_names = {**ecodes.KEY, **ecodes.BTN}

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        name = code_names.get(event.code, f"UNKNOWN({event.code})")
        state = 'pressed' if event.value else 'released'
        print(f"{name} {state}")
