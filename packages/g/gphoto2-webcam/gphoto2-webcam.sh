#!/bin/bash

# modprobe v4l2loopback exclusive_caps=1 card_label="GPhoto2 Webcam" 


device=`v4l2-ctl --list-devices | while read header; do echo $header | grep v4l2loopback > /dev/null && read device && echo $device ; done`

echo "Starting preview capture feed to $device ... press ctrl-c to terminate... "

gphoto2 --stdout --capture-movie | ffmpeg -i - -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 $device
