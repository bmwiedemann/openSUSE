#!/bin/sh
#
#	AIDE _Example_ Cron Script 
#
#	Use at your own risk!
#
#	Matthias G. Eckermann <mge@suse.de>
#

AIDEBINARY=/usr/bin/aide
AIDECONFIG=/etc/aide.conf
AIDEDOMOUNT=
AIDERODEVICE=
MOUNT=/bin/mount
UMOUNT=/bin/umount

#
# if you want to have the aide database on a CDROM,
# then play with these options:
#
#AIDERODEVICE=/media/cdrom
#AIDEDOMOUNT="yes" # some non-zero-string
#AIDECONFIG=/media/cdrom/aide.conf

if [ ".$AIDEDOMOUNT" != "." ] && [ ".$AIDERODEVICE" != "." ] ; then
	echo "mounting $AIDERODEVICE"
	$MOUNT $AIDERODEVICE
fi

if [ -x $AIDEBINARY -a $AIDECONFIG ]; then
	$AIDEBINARY --config=$AIDECONFIG --check
fi

if [ ".$AIDEDOMOUNT" != "." ] && [ ".$AIDERODEVICE" != "." ] ; then
	echo "unmounting $AIDERODEVICE"
	$UMOUNT $AIDERODEVICE
fi

