#
# spec file for package rshim
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Mellanox Technologies. All Rights Reserved.
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


Name:           mlxbf-bootctl
Version:        1.1.6.11
Release:        0
Summary:        User-space driver for Mellanox BlueField SoC
License:        BSD-2-Clause
Group:          System/Management
URL:            https://github.com/Mellanox/mlxbf-bootctl.git
Source0:        %{name}-%{version}.tar
ExclusiveArch:  aarch64

%description
mlxbf-bootctl is used to control the two boot firmware partitions present on most Mellanox BlueField devices.

%prep
%setup -q

%build
%make_build

%install
mkdir -p %{buildroot}%{_sbindir}
install -c -m 0755 mlxbf-bootctl %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8

%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
