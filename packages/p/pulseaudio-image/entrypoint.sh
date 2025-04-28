#!/bin/bash

chown root:audio /dev/snd/*

exec /usr/bin/pulseaudio -vvv --log-target=stderr