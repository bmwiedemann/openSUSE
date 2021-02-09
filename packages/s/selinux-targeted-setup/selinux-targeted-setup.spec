#
# spec file for package selinux-targeted-setup
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _buildshell /bin/bash
Name:           selinux-targeted-setup
Version:        20201215
Release:        0
Summary:        Metapackage that enables a targeted SELinux policy
License:        GPL-2.0-or-later
Group:          System/Management
BuildArch:      noarch
BuildRequires:  update-bootloader-rpm-macros
Requires:       selinux-policy-targeted
Requires(post): selinux-policy-targeted
Recommends:     container-selinux
%{update_bootloader_requires}

%description
Metapackage that enables a targeted SELinux policy.

%prep

%build

%install

%post -p /bin/bash
GRUB_CFG=/etc/default/grub
SELINUX_CFG=/etc/selinux/config
LABEL_CFG1=/.autorelabel
LABEL_CFG2=/etc/selinux/.autorelabel

if [[ -f $GRUB_CFG ]]; then
  if [[ ! $(grep "^GRUB_CMDLINE_LINUX_DEFAULT=" $GRUB_CFG | grep security=selinux) ]]; then
    sed -i -e 's|\(^GRUB_CMDLINE_LINUX_DEFAULT=.*\)"|\1 security=selinux selinux=1"|g' $GRUB_CFG
  fi
fi

if [[ -f $SELINUX_CFG ]]; then
  sed -i -e 's|^SELINUX=.*|SELINUX=enforcing|g' \
      -e 's|^SELINUXTYPE=.*|SELINUXTYPE=targeted|g' \
      $SELINUX_CFG
fi

if [[ -f $LABEL_CFG1 ]]; then
  mv $LABEL_CFG1 $LABEL_CFG2
fi

%{?regenerate_initrd_post}
%update_bootloader_refresh_post

%posttrans
%{?regenerate_initrd_posttrans}
%update_bootloader_posttrans

%postun -p /bin/bash
GRUB_CFG=/etc/default/grub
SELINUX_CFG=/etc/selinux/config

if [[ -f $GRUB_CFG ]]; then
  LINE=$(grep "^GRUB_CMDLINE_LINUX_DEFAULT=" $GRUB_CFG)
  LINE=$(sed 's\selinux=1\selinux=0\' <<< $LINE)
  LINE=$(sed 's\security=selinux\\' <<< $LINE)
  LINE=$(sed 's\enforcing=0\\' <<< $LINE)
  sed -i -e 's|\(^GRUB_CMDLINE_LINUX_DEFAULT=.*\)"|\'"${LINE}"'|g' $GRUB_CFG
fi

if [[ -f $SELINUX_CFG ]]; then
  sed -i -e 's|^SELINUX=.*|SELINUX=permissive|g' \
      -e 's|^SELINUXTYPE=.*|SELINUXTYPE=targeted|g' \
      $SELINUX_CFG
fi

%files

%changelog
