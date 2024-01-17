#
# spec file for package ubridge
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


Name:           ubridge
Version:        0.9.18
Release:        0
Summary:        Bridging between UDP tunnels, Ethernet and TAP interfaces
License:        GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/GNS3/ubridge
Source0:        https://github.com/GNS3/ubridge/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libpcap-devel >= 1.5.3
BuildRequires:  libiniparser-devel >= 4.1

%description
uBridge is a simple application to create user-land bridges between
various technologies. Currently bridging between UDP tunnels,
Ethernet and TAP interfaces is supported.  Packet capture is also
supported.

%prep
%setup -q
# remove bundled iniparser
rm -rf src/iniparser

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
%make_build SYSTEM_INIPARSER=1

%install
install -D -m0755 ubridge %{buildroot}%{_bindir}/ubridge

%files
%license LICENSE
%doc README.rst
%{_bindir}/ubridge

%changelog
