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

# Will be recreated by the next rpm(1) run as root user
rm -v /usr/lib/sysimage/rpm/Index.db


#=======================================
# Clean up after zypper if it is present
#---------------------------------------
if command -v zypper > /dev/null; then
    zypper -n clean
fi

rm -rf {/target,}/var/log/{alternatives.log,lastlog,tallylog,zypper.log,zypp/history,YaST2}

exit 0
