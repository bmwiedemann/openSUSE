#
# spec file for package tinyfecvpn
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           tinyfecvpn
Version:        20180820.0
Release:        0
Summary:        A VPN designed for lossy links with build-in FEC
# Bundled libev is licenced under GPL-3.0+ or BSD-2-Clause
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://github.com/wangyu-/tinyfecVPN
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++

%description
A VPN designed for lossy links, with build-in support for Forward Error
Correction (FEC). This can improve network quality on high-latency lossy links.

%prep
%setup -q
sed -i 's|-ggdb||' makefile
sed -i 's|-static||' makefile
sed -i 's|$(shell git rev-parse HEAD)|%{version}|g' makefile

%build
export OPT='%{optflags} -DNOLIMIT'
make %{?_smp_mflags}

%install
install -D -m 0755 tinyvpn %{buildroot}/%{_bindir}/tinyvpn

%files
%license LICENSE.md
%doc README.md doc/*
%{_bindir}/tinyvpn

%changelog
