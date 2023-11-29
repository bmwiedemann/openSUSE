#!/bin/bash

ln -f raspberrypi-firmware.changes raspberrypi-firmware-config.changes
ln -f raspberrypi-firmware.changes raspberrypi-firmware-config-camera.changes
cp raspberrypi-firmware-config.spec raspberrypi-firmware-config-camera.spec
sed -i "s/Name:           raspberrypi-firmware-config/Name:           raspberrypi-firmware-config-camera/" raspberrypi-firmware-config-camera.spec
osc service run format_spec_file
