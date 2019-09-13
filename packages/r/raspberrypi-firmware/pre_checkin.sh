#!/bin/bash

ln -f raspberrypi-firmware.changes raspberrypi-firmware-config.changes
osc service localrun format_spec_file
