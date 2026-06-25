#
# spec file for package elemental
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           elemental
Version:        3.0.0
Release:        0
Summary:        Elemental 3
License:        Apache-2.0
URL:            https://github.com/SUSE/elemental
Source0:        https://github.com/SUSE/elemental/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  rsync
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.26

%description
Elemental is a software stack managing cloud-native, immutable OS and Kubernetes
lifecycles.

%package -n elemental3
Summary:        Elemental 3
Requires:       btrfsmaintenance
Requires:       btrfsprogs
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       gptfdisk
Requires:       grub2-common
Requires:       lvm2
Requires:       mtools
Requires:       rsync
Requires:       snapper
Requires:       udev
Requires:       util-linux-systemd
Requires:       xorriso

%description -n elemental3
Elemental3 is a tool for managing machines using cloud-native
technologies.

%package -n elemental3ctl
Summary:        Elemental 3 control client
Requires:       btrfsprogs
Requires:       coreutils
Requires:       crypto-policies-scripts
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       efibootmgr
Requires:       grub2-common
Requires:       mtools
Requires:       policycoreutils
Requires:       rsync
Requires:       snapper
Requires:       squashfs
Requires:       udev
Requires:       util-linux
Requires:       util-linux-systemd
Requires:       xorriso
Provides:       elemental3-toolkit = %{version}
Obsoletes:      elemental3-toolkit < %{version}

%description -n elemental3ctl
Elemental3ctl is a tool for managing machines using cloud-native
technologies.

%prep
%autosetup -p1 -a1 -n elemental-%{version}

%build
%make_build GIT_TAG='%{version}' GO_EXTRA_ARGS='-trimpath -buildmode=pie' all

%install
install -m 0755 -D build/%{name}3 %{buildroot}/%{_bindir}/%{name}3
install -m 0755 -D build/%{name}3ctl %{buildroot}/%{_bindir}/%{name}3ctl

%check
# tests require root and network
# go test ./...

%files -n elemental3
%license LICENSE
%doc README.md
%{_bindir}/%{name}3

%files -n elemental3ctl
%license LICENSE
%doc README.md
%{_bindir}/%{name}3ctl

%changelog
