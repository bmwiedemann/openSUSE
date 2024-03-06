#!/usr/bin/python3
import hashlib
import sys
import re

def sha256_from_data(data):
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(data)
    return hash_sha256.hexdigest()

lines = open('wireplumber.conf', 'r', encoding='utf-8').readlines()

is_in_device_monitor = False
main_config_content = ''
device_monitors_content = ''
for line in lines:
    if re.match(' *## Device monitors$', line):
        main_config_content += line
        main_config_content += '  # Section moved to a device-monitors.conf file which is provided by the wireplumber-audio package\n\n'
        is_in_device_monitor = True
        continue
    elif re.match(' *## ', line):
        is_in_device_monitor = False

    if is_in_device_monitor:
        device_monitors_content += line
    else:
        main_config_content += line

config_sha256 = sha256_from_data(device_monitors_content.encode('utf-8'))
verified_sha256 = 'bf33d018e5b924da71266636757fa264bc677b945c35e4dcd7f708da42731cc9'
if config_sha256 != verified_sha256:
    print('The "Device monitors" section was modified, please verify that the contents are ok')
    print('and if they are, modify the "verified_sha256" value in this script to')
    print(f'    {config_sha256}')
    print('Current device monitors section is:')
    print(device_monitors_content)
    sys.exit(1)

device_monitors_content = 'wireplumber.components = [\n' + device_monitors_content + ']'

open('wireplumber.conf', 'w', encoding='utf-8').write(main_config_content)
open('wireplumber.conf.d/00-device-monitors.conf', 'w', encoding='utf-8').write(device_monitors_content)
