#
# spec file for package disk-encryption-tool
#
# Copyright (c) 2024 SUSE LLC
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
# icecream 0


%if 0%{?_build_in_place}
%define git_version %(git log '-n1' '--date=format:%Y%m%d' '--no-show-signature' "--pretty=format:+git%cd.%h")
BuildRequires:  git-core
%else
# this is required for obs' source validator. It's
# 20-files-present-and-referenced ignores all conditionals. So the
# definition of git_version actually happens always.
%define git_version %{nil}
%endif

Name:           disk-encryption-tool
Version:        1+git20240702.24fe41e%{git_version}
Release:        0
Summary:        Tool to reencrypt kiwi raw images
License:        MIT
URL:            https://github.com/lnussel/disk-encryption-tool
Source:         disk-encryption-tool-%{version}.tar
Requires:       cryptsetup
Requires:       keyutils
Requires:       pcr-oracle
# something needs to require it. Can be us.
Requires:       tpm2.0-tools
Requires:       qrencode
ExclusiveArch:  aarch64 ppc64le riscv64 x86_64

%description
Convert a plain text kiwi image into one with LUKS full disk
encryption. Supports both raw and qcow2 images. It assumes that the
third partition is the root fs using btrfs.
After encrypting the disk, the fs is mounted and a new initrd
created as well as the grub2 config adjusted.

%prep
%setup -q

%build

%install
mkdir -p %buildroot/usr/lib/dracut/modules.d/95disk-encryption-tool
for i in disk-encryption-tool{,-dracut,-dracut.service}  module-setup.sh generate-recovery-key; do
  cp "$i" %buildroot/usr/lib/dracut/modules.d/95disk-encryption-tool/"$i"
done
mkdir -p %buildroot/usr/bin
ln -s ../lib/dracut/modules.d/95disk-encryption-tool/disk-encryption-tool %buildroot/usr/bin
ln -s ../lib/dracut/modules.d/95disk-encryption-tool/generate-recovery-key %buildroot/usr/bin
install -D -m 644 jeos-firstboot-diskencrypt-override.conf \
	%{buildroot}/usr/lib/systemd/system/jeos-firstboot.service.d/jeos-firstboot-diskencrypt-override.conf
install -D -m 644 jeos-firstboot-enroll %buildroot/usr/share/jeos-firstboot/modules/enroll

%files
%license LICENSE
/usr/bin/disk-encryption-tool
/usr/bin/generate-recovery-key
%dir /usr/lib/dracut
%dir /usr/lib/dracut/modules.d
/usr/lib/dracut/modules.d/95disk-encryption-tool
%dir /usr/share/jeos-firstboot
%dir /usr/share/jeos-firstboot/modules
/usr/share/jeos-firstboot/modules/enroll
%dir /usr/lib/systemd/system/jeos-firstboot.service.d
/usr/lib/systemd/system/jeos-firstboot.service.d/jeos-firstboot-diskencrypt-override.conf

%changelog
