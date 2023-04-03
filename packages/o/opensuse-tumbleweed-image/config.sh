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

# Remove various log files. While it's possible to just rm -rf /var/log/*, that
# would also remove some package owned directories (not %ghost) and some files
# are actually wanted, like lastlog in the !docker case.
# For those wondering about YaST2 here: Kiwi writes /etc/hosts, so the version
# from the netcfg package ends up as /etc/hosts.rpmnew, which zypper writes a
# letter about to /var/log/YaST2/config_diff_2022_03_06.log. Kiwi fixes this,
# but the log file remains.
rm -rf /var/log/{zypper.log,zypp/history,YaST2}

# Remove the entire zypper cache content (not the dir itself, owned by libzypp)
rm -rf /var/cache/zypp/*

# Assign a fixed architecture in zypp.conf, to use the container's arch even if
# the host arch differs (e.g. docker with --platform doesn't affect uname)
arch=$(rpm -q --qf %{arch} glibc)
if [ "$arch" = "i586" ] || [ "$arch" = "i686" ]; then
	sed -i "s/^# arch =.*\$/arch = i686/" /etc/zypp/zypp.conf
	# Verify that it's applied
	grep -q '^arch =' /etc/zypp/zypp.conf
fi

if [[ "$kiwi_profiles" == *"docker"* ]]; then
	# Hack! The go container management tools can't handle sparse files:
	# https://github.com/golang/go/issues/13548
	# When lastlog doesn't exist, useradd doesn't attempt to reserve space.
	rm -f /var/log/lastlog
fi

if [[ "$kiwi_profiles" == *"networkd"* ]]; then
	systemctl enable systemd-networkd
	systemctl enable systemd-resolved
	# FIXME: kiwi deletes /etc/resolv.conf so we have to use tmpfiles here.
	# Should come via some preset package anyways I guess.
	echo "L /etc/resolv.conf - - - - /run/systemd/resolve/stub-resolv.conf" > /etc/tmpfiles.d/stub-resolv.conf
fi

exit 0
