#!/bin/bash
# vim:sw=4 et
# This script is called automatically during autobuild checkin.

cp -lf dbus-1.changes dbus-1-x11.changes

osc service localrun format_spec_file
