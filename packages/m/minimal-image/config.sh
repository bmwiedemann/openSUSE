#!/bin/bash
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: (c) 2022 SUSE LLC

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



#=======================================
# Clean up after zypper if it is present
#---------------------------------------
if command -v zypper > /dev/null; then
    zypper -n clean
fi

rm -rf /var/log/zypp

exit 0
