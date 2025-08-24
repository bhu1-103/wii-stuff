# wii-stuff
cool stuff i learnt about wii

## setting it up

`bluetoothctl;`

`power on;`
`agent on;`
`default-agent;`
`scan on;`
`pair 00:1B:11:22:33:44;`
`connect 00:1B:11:22:33:44;`
`trust 00:1B:11:22:33:44;`

replace this mac address with the mac address of your wiimote

everytime you connect, forget the device and reconnect, as it will start asking for a password

range of accelerometer for wiimote and nunchuck is -512 to +512 units
