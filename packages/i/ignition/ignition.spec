#
# spec file for package ignition
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ignition
Version:        2.3.0
Release:        0
Summary:        First boot installer and configuration tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/coreos/ignition
Source:         %{name}-%{version}.tar.xz
Patch2:         0002-allow-multiple-mounts-of-same-device.patch
Requires:       dracut
Recommends:     /sbin/mkfs.btrfs
Recommends:     /sbin/mkfs.ext4
Recommends:     /sbin/mkfs.vfat
Recommends:     /sbin/mkfs.xfs
Recommends:     /sbin/mkswap
Recommends:     /sbin/udevadm
Recommends:     /usr/sbin/groupadd
Recommends:     /usr/sbin/sgdisk
Recommends:     /usr/sbin/useradd
Recommends:     /usr/sbin/usermod
Suggests:       /sbin/mdadm
BuildRequires:  dracut
BuildRequires:  libblkid-devel
BuildRequires:  golang(API) >= 1.12

%description
Ignition is an utility to manipulate disks and configuration files
during the initramfs. This includes partitioning disks, formatting
partitions, writing files (regular files, systemd units, etc.), and
creating users.
On first boot, Ignition reads its configuration from a source of truth
(remote URL, network metadata service, hypervisor bridge, etc.) and
applies the configuration.

%prep
%setup -q
%patch2 -p1

%build
sed -i -e 's|go build -ldflags|go build -buildmode=pie -ldflags|g' build
env VERSION=%{version} GLDFLAGS='-X github.com/coreos/ignition/v2/internal/distro.selinuxRelabel=false -X github.com/coreos/ignition/v2/internal/distro.writeAuthorizedKeysFragment=false ' bash -x ./build

%install
install -d %{buildroot}%{_prefix}/lib/dracut/modules.d/30ignition
install -p -m 0755 bin/*/ignition %{buildroot}%{_prefix}/lib/dracut/modules.d/30ignition
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/*/ignition-validate %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md doc
%{_prefix}/lib/dracut/modules.d/30ignition
%{_bindir}/ignition-validate

%changelog
