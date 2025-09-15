#!/bin/bash

test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

if [[ $kiwi_displayname =~ "Leap" ]]; then
  export defaultName=$(echo $kiwi_displayname | awk -F'-' '{print $1"-"$2"-"$3}')
elif [[ $kiwi_displayname =~ "Enterprise-15" ]]; then
  export defaultName=$(echo $kiwi_displayname | awk -F'-' '{print $1"-"$2"-"$3"-"$4"-"$5}')
  export versionInfo=$(echo $kiwi_displayname | awk -F'-' '{print $4"-"$5}')
  export archInfo=$(uname -i)
elif [[ $kiwi_displayname =~ "Enterprise-16" ]]; then
  export defaultName=$(echo $kiwi_displayname | awk -F'-' '{print $1"-"$2"-"$3"-"$4}')
  export versionInfo=$(echo $kiwi_displayname | awk -F'-' '{print $4}')
  export archInfo=$(uname -i)
else
  export defaultName=$(echo $kiwi_displayname | awk -F'-' '{print $1"-"$2}')
fi

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
  echo "I am grepping for opensuse in os-release and MATCHED ..."
  #add-yast-repos
  #zypper --non-interactive rm -u live-add-yast-repos
fi

source /etc/os-release
if (printf "$PRETTY_NAME" | grep -iq 'suse linux enterprise'); then
  # Add [free] SLE_BCI repo - https://jira.suse.com/browse/PED-8754
  zypper --non-interactive addrepo --priority 100 "https://updates.suse.com/SUSE/Products/SLE-BCI/$versionInfo/$archInfo/product/" SLE_BCI
fi

cat <<EOF >/etc/wsl.conf
[boot]
systemd=true
EOF

cat <<EOF >/etc/wsl-distribution.conf
[oobe]
command = /usr/sbin/wsl-firstboot
defaultUid = 1000
defaultName = $defaultName

[shortcut]
icon = /usr/share/pixmaps/$defaultName.ico
EOF

zypper --non-interactive addlock -m 'Conflicts with wsl-firstboot.' jeos-firstboot

exit 0
