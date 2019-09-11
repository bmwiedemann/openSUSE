#!/usr/bin/python3
import configparser
import itertools
import os
import sys

xdg_config_home = os.environ.get("XDG_CONFIG_HOME",
                                 os.path.expanduser("~/.config"))
proc_env = os.environ
conf_parser = configparser.SafeConfigParser()

for conf_file in ("/etc/apulse.conf",
                  os.path.join(xdg_config_home, "apulse.conf")):
    if os.access(conf_file, os.R_OK):
        with open(conf_file, "r") as conf:
            conf = itertools.chain(("[0]",), conf)
            conf_parser.read_file(conf)

playback_device = conf_parser.get("0", "playback-device", fallback="default")
capture_device = conf_parser.get("0", "capture-device", fallback="default")

if "APULSE_PLAYBACK_DEVICE" not in proc_env:
    proc_env["APULSE_PLAYBACK_DEVICE"] = playback_device
if "APULSE_CAPTURE_DEVICE" not in proc_env:
    proc_env["APULSE_CAPTURE_DEVICE"] = capture_device

ld_libpath = os.environ.get("LD_LIBRARY_PATH", "")
proc_env["LD_LIBRARY_PATH"] = "/usr/$LIB/apulse" + \
                              (":" if ld_libpath else "") + ld_libpath

os.execvpe(sys.argv[1], sys.argv[1:], proc_env)
