#!/bin/bash

# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

set -euo pipefail

echo "Configure image: [$kiwi_iname]..."

#======================================
# Setup baseproduct link
#--------------------------------------
suseSetupProduct

#======================================
# Import repositories' keys
#--------------------------------------
suseImportBuildKey

#======================================
# Add repos from control.xml
#--------------------------------------
if grep -q opensuse /usr/lib/os-release || grep -q opensuse /etc/os-release; then
	add-yast-repos
	zypper --non-interactive rm -u live-add-yast-repos
fi

# XXX: workaround until we have a launcher that sets the password properly
#if ! grep -q 12-SP5 /etc/os-release 2>/dev/null; then
#	sed -i -e 's/root:\*:/root::/' /etc/shadow
#	pam-config -a --nullok
#	echo '%users ALL=(ALL) NOPASSWD: ALL' /etc/sudoers.d/wsl
#fi

#======================================
# Disable recommends
#--------------------------------------
sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf

if [ -e /etc/sysconfig/firstboot -a -e /etc/YaST2/firstboot-wsl.xml ]; then
	# set custom firstboot control file
	sed -ie 's,^\(FIRSTBOOT_CONTROL_FILE\)=.*,\1="/etc/YaST2/firstboot-wsl.xml",' \
		/etc/sysconfig/firstboot
fi

# Remove zypp uuid (bsc#1098535)
rm -f /var/lib/zypp/AnonymousUniqueId

# WSL specific tweaks
# XXX: not sure what this is for. Was found in root.tar.bz2. Needs to be confirmed
mkdir -p etc/apache2/conf.d
echo AcceptFilter http none > etc/apache2/conf.d/wsl.conf

exit 0
