#!/bin/bash
test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

set -euxo pipefail

echo "Configure image: [$kiwi_iname]..."

#======================================
# Import repositories' keys
#--------------------------------------
suseImportBuildKey

#======================================
# Add repos from control.xml
#--------------------------------------
add-yast-repos
zypper --non-interactive rm -u live-add-yast-repos

#======================================
# Disable recommends
#--------------------------------------
sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf

#======================================
# Exclude docs intallation
#--------------------------------------
sed -i 's/.*rpm.install.excludedocs.*/rpm.install.excludedocs = yes/g' /etc/zypp/zypp.conf

#======================================
# Remove locale files
#--------------------------------------
shopt -s globstar
rm -f /usr/share/locale/**/*.mo

# Remove zypp uuid (bsc#1098535)
rm -f /var/lib/zypp/AnonymousUniqueId

if [[ "$kiwi_profiles" == *"networkd"* ]]; then
	systemctl enable systemd-networkd
	systemctl enable systemd-resolved
	# FIXME: kiwi deletes /etc/resolv.conf so we have to use tmpfiles here.
	# Should come via some preset package anyways I guess.
	echo "L /etc/resolv.conf - - - - /run/systemd/resolve/stub-resolv.conf" > /etc/tmpfiles.d/stub-resolv.conf
fi

exit 0
