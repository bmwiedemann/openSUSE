#!/bin/bash

# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019-2023 SUSE LLC
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
### 20260216: libzypp v17.38.2 removes /etc/zypp/zypp.conf (by default)
###   and uses a very basic /usr/etc/zypp/zypp.conf which doesn't include
###   any solver stanzas
#sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf
### This could potentially put it back in place, but image size was no different
###   with/without it
#echo "solver.onlyRequires = true" >>/usr/etc/zypp/zypp.conf.d/01-onlyRequires.conf
#####

if [ -e /etc/sysconfig/firstboot -a -e /etc/YaST2/firstboot-wsl.xml ]; then
	# set custom firstboot control file
	sed -ie 's,^\(FIRSTBOOT_CONTROL_FILE\)=.*,\1="/etc/YaST2/firstboot-wsl.xml",' \
		/etc/sysconfig/firstboot
fi

if ! (grep -q opensuse /usr/lib/os-release || grep -q opensuse /etc/os-release); then
  source /usr/share/wsl-appx/DOTsettings
  # MAJOR_VER,SP_VER, and OARCH come from wsl-appx DOTsettings file (sourced above)
  # Add [free] SLE_BCI repo - https://jira.suse.com/browse/PED-8754
  zypper --non-interactive addrepo --priority 100 "https://updates.suse.com/SUSE/Products/SLE-BCI/$MAJOR_VER-SP$SP_VER/$OARCH/product/" SLE_BCI
  # Inject curated text into /etc/YaST2/products.yaml
  cat << EOF > /etc/YaST2/products.yaml
- display_name: "SUSE Linux Enterprise Server $MAJOR_VER SP$SP_VER"
  name: "SLES"
  register_target: "sle-$MAJOR_VER-x86_64"
  version: "$MAJOR_VER.$SP_VER"
  default: true
- display_name: "SUSE Linux Enterprise Desktop $MAJOR_VER SP$SP_VER"
  name: "SLED"
  register_target: "sle-$MAJOR_VER-x86_64"
  version: "$MAJOR_VER.$SP_VER"
EOF
fi

# Always remove wsl-appx so future rebuilds of that package
#   don't cause zypper dup conflict
zypper --non-interactive rm -u wsl-appx

# Remove zypp uuid (bsc#1098535)
rm -f /var/lib/zypp/AnonymousUniqueId

# WSL specific tweaks
# XXX: not sure what this is for. Was found in root.tar.bz2. Needs to be confirmed
#mkdir -p etc/apache2/conf.d
#echo AcceptFilter http none > etc/apache2/conf.d/wsl.conf

# workaround for broken wslfs (boo#1159195). Note that as of 2020-02-06 kiwi
# resets /etc/fstab: https://github.com/OSInside/kiwi/issues/1329
echo "tmpfs /var/tmp tmpfs defaults 0 0" >> /etc/fstab

exit 0
