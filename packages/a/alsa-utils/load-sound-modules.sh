#!/bin/sh

test -r /etc/sysconfig/sound && . /etc/sysconfig/sound

if [ "$LOAD_OSS_EMUL_MODULES" = "yes" ]; then
    /sbin/modprobe -q snd-mixer-oss
    /sbin/modprobe -q snd-pcm-oss
fi

if [ "$LOAD_SEQUENCER" = "yes" ]; then
    /sbin/modprobe -q snd-seq
fi

if [ -r /proc/asound/seq/drivers ]; then
    OLDIFS="$IFS"
    IFS=","
    while read t x c; do
	/sbin/modprobe -q $t
    done < /proc/asound/seq/drivers
    IFS="$OLDIFS"
fi

if [ -d /proc/asound/seq ]; then
    if [ "$LOAD_OSS_SEQ_MODULE" = "yes" ]; then
	/sbin/modprobe -q snd-seq-oss
    fi
fi
	
exit 0
