#!/bin/sh
#Simple script to start iwscanner

KDESU=/usr/bin/kdesu
GNOMESU=/usr/bin/gnomesu
XDGSU=/usr/bin/xdg-su

if [ -e "$KDESU" ]
   then
   $KDESU -c /usr/share/iwscanner/iwscanner.py
elif [ -e "$GNOMESU" ]
   then
   $GNOMESU -c /usr/share/iwscanner/iwscanner.py
elif [ -e "$XDGSU" ]
   then
   $XDGSU -c /usr/share/iwscanner/iwscanner.py
else
   echo "Unable to find suitable su application, please install xdg-utils"
fi