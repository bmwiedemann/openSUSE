#!/bin/sh

cd /usr/lib/rescue && exec /usr/bin/java \
-jar Rescue.jar "${@}"
