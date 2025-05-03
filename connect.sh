#!/usr/bin/zsh

bluetoothctl scan on
bluetoothctl remove 00:1B:7A:06:11:DF
bluetoothctl pair 00:1B:7A:06:11:DF
bluetoothctl connect 00:1B:7A:06:11:DF
