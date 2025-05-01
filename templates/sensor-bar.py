from evdev import InputDevice, ecodes

dev = InputDevice('/dev/input/event17')

dot_labels = {
    ecodes.ABS_HAT0X: "Dot 1 X", ecodes.ABS_HAT0Y: "Dot 1 Y",
    ecodes.ABS_HAT1X: "Dot 2 X", ecodes.ABS_HAT1Y: "Dot 2 Y",
    ecodes.ABS_HAT2X: "Dot 3 X", ecodes.ABS_HAT2Y: "Dot 3 Y",
    ecodes.ABS_HAT3X: "Dot 4 X", ecodes.ABS_HAT3Y: "Dot 4 Y",
}

for event in dev.read_loop():
    if event.type == ecodes.EV_ABS and event.code in dot_labels:
        print(f"{dot_labels[event.code]}: {event.value}")
