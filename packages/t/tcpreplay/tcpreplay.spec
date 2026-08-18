#
# spec file for package tcpreplay
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


Name:           tcpreplay
Version:        4.6.1
Release:        0
Summary:        Network analysis and testing tools
License:        GPL-3.0-only
URL:            https://tcpreplay.appneta.com/
Source0:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  libdnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  tcpdump
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
Requires:       tcpdump

%description
Tcpreplay is a suite of utilities for editing and replaying
previously captured network traffic. It was originally designed to
replay malicious traffic patterns to Intrusion Detection/Prevention
Systems, and is meanwhile capable of replaying to web servers. It
supports switches, routers and IP Flow/NetFlow appliances.

%prep
%autosetup -p1

%build
%configure \
  --enable-dynamic-link
%make_build

%install
%make_install
# 4.6.0 started installing the replay engine as a STATIC library plus its
# headers and pkgconfig file.  There is no configure switch to turn that
# off, and openSUSE does not ship static-only libraries without a consumer
# to justify them -- nothing in Factory links against libtcpreplay.  Drop
# them and keep this package what it has always been: the command-line
# tools.  Revisit if upstream grows a shared library or a consumer appears.
rm -r %{buildroot}%{_includedir}/%{name}
rm %{buildroot}%{_libdir}/lib%{name}.a
rm %{buildroot}%{_libdir}/pkgconfig/lib%{name}.pc

%check
# 4.6.1 added a dependency-free unit suite plus a fuzz-corpus replay, both
# wired into "make check".  The integration suite under test/ is deliberately
# not part of it -- that one needs root and a live NIC -- so this stays
# runnable in the build root.
%make_build check

%files
%license docs/LICENSE
%doc docs/CHANGELOG
%{_bindir}/tcpbridge
%{_bindir}/tcpcapinfo
%{_bindir}/tcpliveplay
%{_bindir}/tcpprep
%{_bindir}/tcpreplay
%{_bindir}/tcpreplay-edit
%{_bindir}/tcprewrite
%{_mandir}/man1/tcpbridge.1%{?ext_man}
%{_mandir}/man1/tcpcapinfo.1%{?ext_man}
%{_mandir}/man1/tcpliveplay.1%{?ext_man}
%{_mandir}/man1/tcpprep.1%{?ext_man}
%{_mandir}/man1/tcpreplay-edit.1%{?ext_man}
%{_mandir}/man1/tcpreplay.1%{?ext_man}
%{_mandir}/man1/tcprewrite.1%{?ext_man}

%changelog
