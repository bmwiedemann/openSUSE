#!/usr/bin/python3
#
# A program to check the validity of topics.list
#
# usage: check-topic.py WHENCE KERNEL-RPMs...
#

from sys import argv
from fwtopics import FWTopics

if __name__ == '__main__':
    fw = FWTopics()
    argv.pop(0)
    fw.parse_whence(argv.pop(0))
    for arg in argv:
        fw.scan_firmware(arg, fw.check_module())
