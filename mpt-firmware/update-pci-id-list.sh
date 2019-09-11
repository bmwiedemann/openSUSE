#!/bin/bash

KVERS=$1

if [ -z "$KVERS" ]; then
    for dir in /lib/modules/2.6.*; do
	if [ -f $dir/modules.alias ] ; then
	    MODPATH=$dir/modules.alias
	fi
    done
    if [ -z "$MODPATH" ] ; then
	echo 'Cannot determine kernel version'
	exit 1
    else
	echo "Using $MODPATH"
    fi
else
    MODPATH=/lib/modules/$KVERS/modules.alias
fi

if [ ! -f $MODPATH ] ; then
    echo '$MODPATH not found'
    exit 1
fi

spi_list=$(grep mptspi $MODPATH | sed 's/\(alias\) \(pci:.*\*\) \(mpt.*\)/\2/g')
echo "/^# Module: mptspi/
kb
+
/^#/
-
ke
'b,'ed
i
# Module: mptspi.ko
$(for id in $spi_list; do echo Supplements: modalias\($id\); done)
.
w
q " | ed $2

fc_list=$(grep mptfc $MODPATH | sed 's/\(alias\) \(pci:.*\*\) \(mpt.*\)/\2/g')
echo "/^# Module: mptfc/
kb
+
/^#/
-
ke
'b,'ed
i
# Module: mptfc.ko
$(for id in $fc_list; do echo Supplements: modalias\($id\); done)
.
w
q " | ed $2

sas_list=$(grep mptsas $MODPATH | sed 's/\(alias\) \(pci:.*\*\) \(mpt.*\)/\2/g')
echo "/^# Module: mptsas/
kb
+
/^#/
-
ke
'b,'ed
i
# Module: mptsas.ko
$(for id in $sas_list; do echo Supplements: modalias\($id\); done)
.
w
q " | ed $2

