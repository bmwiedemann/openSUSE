#!/bin/bash

# Script to update extpack
# The idea for this method and the original code came from Larry Len Rainey.
#
# This implementation by Larry Finger

# Define some symbols and determine the current version of VB

VBOXMANAGE=/usr/bin/VBoxManage
AWK=/usr/bin/awk
GREP=/usr/bin/grep
WGET=/usr/bin/wget
VBOX_VERSION=`$VBOXMANAGE --version | $AWK -F_ {'print $1'}`

# Define a symbol for the name of the extpack matching the VB version
VBOX_EXT=`echo Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VERSION}.vbox-extpack`

# Full path to extpack license file
LICENSE_PATH="/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack-license.rtf"

# Determine the installed version of extpack, if any.
EXTPACK_CURRENT=`$VBOXMANAGE list extpacks | $GREP -A1 "Oracle VM VirtualBox Extension Pack" | $GREP Version | $AWK -F\  {'print $2'}`

# The extpacks are licensed under a Personal Use and Evaluation License
# At some point, the user must agree to the conditions of that license.
# If no extpack is installed on this system, then there is no agreement,
# thus this script cannot install the extpack.
#
# This situation applies to new installations that could conform to the license,
# but more importantly, it handles commercial setups that have not purchased
# the necessary license.
# Check if extpack is currently installed. If not exit
if [ -z $EXTPACK_CURRENT ]; then
	exit 0
fi
#
# An extpack has been installed on this system. Now we need to check if
# it was issued under the current version of the license.

#Note to maintainers: The "version 11" in the next command must be changed
# manually when Oracle revises the license.

LICENSE_CHECK=`$GREP "version 11" $LICENSE_PATH | $AWK -F\  {'print $2'}`
if [ -z $LICENSE_CHECK ]; then
# New license version does not match the current installation.
# The user will need to agree to the new version, thus we do nothing here.
	exit 0
fi
if [ $VBOX_VERSION == $EXTPACK_CURRENT ]; then
# The extpack currently installed matches - we are done
	exit 0
fi

# A new version of extpack is needed - switch to directory that can be written, and download it
pushd ~ > /dev/null 2>&1
$WGET https://download.virtualbox.org/virtualbox/$VBOX_VERSION/$VBOX_EXT > /dev/null 2>&1

# Now install it
echo Y | $VBOXMANAGE extpack install --replace $VBOX_EXT > /dev/null 2>&1

# Clean up by deleting downloaded file and restoring the original working directory
rm -f $VBOX_EXT
popd ~ > /dev/null 2>&1
