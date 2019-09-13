#!/usr/bin/python3
#
# A program to update aliases.list from the given kernel binary rpms
#
# usage: update-aliases.py KERNEL-RPMs...
#

from sys import argv
from fwtopics import FWTopics

if __name__ == '__main__':
    fw = FWTopics()
    fw.read_aliases()
    argv.pop(0)
    for arg in argv:
        fw.scan_firmware(arg, fw.update_alias())
    fw.write_aliases()
