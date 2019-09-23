#!/bin/bash
#
# Copyright (c) 2017 Scorpio IT, Deidesheim, Germany
# All rights reserved
#
# Author: Christian Wittmer <rpm@scorpio-it.net>
#

export LANG=POSIX
PATH="/bin:/usr/bin:/sbin:/usr/sbin"

# Check for existence of needed config file and read it
OTRS_SYSCONFIG=/etc/sysconfig/otrs
test -r $OTRS_SYSCONFIG || { echo "$OTRS_SYSCONFIG does not exist";
        if [ "$1" = "stop" ]; then exit 0;
        else exit 6; fi; }

# Read config
. $OTRS_SYSCONFIG

# --
# prepare cron stuff
# --

if test $OTRS_CRON_RUNNING -gt 0; then
    if [[ -d $OTRS_CRON_DIR ]]; then
        cd $OTRS_CRON_DIR
        /bin/ls * | /usr/bin/grep -v '.dist' | /usr/bin/grep -v '.save' | /usr/bin/grep -v 'CVS' | /usr/bin/grep -v '.rpm' | \
            /usr/bin/xargs cat > $OTRS_CRON_TMP_FILE
    fi
fi
