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
# Disable recommends
#--------------------------------------
echo "install_weak_deps=False" >> /etc/dnf/dnf.conf

#======================================
# Exclude docs intallation
#--------------------------------------
echo "tsflags=nodocs" >> /etc/dnf/dnf.conf

#======================================
# Remove locale files
#--------------------------------------
shopt -s globstar
rm -f /usr/share/locale/**/*.mo

# Clean up any leftover cache files
rm -rf /var/cache/dnf/*
rm -rf /var/cache/yum/*

if [[ "$kiwi_profiles" == *"networkd"* ]]; then
	systemctl enable systemd-networkd
	systemctl enable systemd-resolved
	# FIXME: kiwi deletes /etc/resolv.conf so we have to use tmpfiles here.
	# Should come via some preset package anyways I guess.
	echo "L /etc/resolv.conf - - - - /run/systemd/resolve/stub-resolv.conf" > /etc/tmpfiles.d/stub-resolv.conf
fi

exit 0
