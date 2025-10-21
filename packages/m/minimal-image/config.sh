#!/bin/bash
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (c) 2022-2025 SUSE LLC

set -euo pipefail

test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

echo "Configure image: [$kiwi_iname]..."

#============================================
# Import repositories' keys if rpm is present
#--------------------------------------------
if command -v rpm > /dev/null; then
    suseImportBuildKey
fi


#==========================================
# Remove compat-usrmerge-tools if installed
#------------------------------------------
if rpm -q compat-usrmerge-tools; then
    rpm -e compat-usrmerge-tools
fi

# don't have duplicate licenses of the same type
jdupes -1 -L -r /usr/share/licenses
rpm -e jdupes

# set the day of last password change to empty
sed -i 's/^\([^:]*:[^:]*:\)[^:]*\(:.*\)$/\1\2/' /etc/shadow
rpm -e sed

# not making sense in a zypper-free image
rm -vf /var/lib/zypp/AutoInstalled

# includes device and inode numbers that change on deploy
rm -vf /var/cache/ldconfig/aux-cache

# Will be recreated by the next rpm(1) run as root user
rm -vf /usr/lib/sysimage/rpm/Index.db


#=======================================
# Clean up after zypper if it is present
#---------------------------------------
if command -v zypper > /dev/null; then
    zypper -n clean -a
fi

#=============================================
# Clean up logs and temporary files if present
#---------------------------------------------
rm -rf {/target,}/var/log/{alternatives.log,lastlog,tallylog,zypper.log,zypp/history,YaST2}; \
    rm -rf {/target,}/run/*; \
    rm -f {/target,}/etc/{shadow-,group-,passwd-,.pwd.lock}; \
    rm -f {/target,}/usr/lib/sysimage/rpm/.rpm.lock; \
    rm -f {/target,}/var/cache/ldconfig/aux-cache; \
    command -v zypper >/dev/null 2>&1 || rm -f /var/lib/zypp/AutoInstalled


exit 0
