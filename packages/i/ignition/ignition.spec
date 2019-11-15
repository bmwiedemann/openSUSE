#
# spec file for package ignition
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.0.1+git20191106.809f44a
Release:        0
Summary:        First boot installer and configuration tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/coreos/ignition
Source:         %{name}-%{version}.tar.xz
Requires:       dracut
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

%build
sed -i -e 's|go build -ldflags|go build -buildmode=pie -ldflags|g' build
env VERSION=%{version} bash -x ./build

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
