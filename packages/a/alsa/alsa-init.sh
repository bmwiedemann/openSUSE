#!/bin/sh
# alsa-init card#

/usr/bin/set_default_volume -f $1 >/dev/null 2>&1
test -s /var/lib/alsa/asound.state && /usr/sbin/alsactl -F restore $1 >/dev/null 2>&1
# increase buffer-preallocation size (for PA)
if [ -f /proc/asound/card$1/pcm0p/sub0/prealloc_max ]; then
    [ $(cat /proc/asound/card$1/pcm0p/sub0/prealloc_max) -le 1024 ] ||
	echo 1024 > /proc/asound/card$1/pcm0p/sub0/prealloc
fi

exit 0
