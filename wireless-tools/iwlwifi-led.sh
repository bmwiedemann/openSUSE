#!/bin/sh

if test -f /sys$DEVPATH/trigger ; then
	phyno=${DEVPATH##*/iwl-phy}
	phyno=${phyno%%:assoc}
	phyno=${phyno%%:}

	# possible triggers:
	# - phy${phyno}rx
	# - phy${phyno}tx
	# - phy${phyno}assoc
	# - phy${phyno}radio
	# - none
	echo "phy${phyno}rx" >> /sys$DEVPATH/trigger
fi
