# trigger removal of driver modules with non-existing or wrong
# firmware when (new) firmware gets installed
if test -e /sys/module/nvidia \
    && cat /sys/class/drm/card*/device/vendor | grep -vq 10de; then
    rmmod nvidia_drm nvidia_uvm nvidia_modeset video nvidia &> /dev/null
fi
