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
Version:        4.5.3
Release:        0
Summary:        Network analysis and testing tools
License:        GPL-3.0-only
URL:            https://tcpreplay.appneta.com/
Source0:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# CVE-2025-8746 [bsc#1247917], improper input validation and memory bounds checking when processing certain malformed configuration files
Patch0:         tcpreplay-CVE-2025-8746.patch
# Fix the __GLIBC_MINOR typo in txring.h and include <linux/if_packet.h>,
# which is what actually defines the PACKET_TX_RING API - sent upstream
Patch1:         tcpreplay-fix-txring-includes.patch
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
# The bundled libopts (autoopts) is not C23-clean, so it needs an older
# language level than gcc >= 15's -std=gnu23 default.  Pin it for that
# directory only: pinning the whole tree also drags configure's TX_RING
# probe below C23, where <netpacket/packet.h> and <linux/if_packet.h>
# cannot be included together, which silently disabled HAVE_TX_RING and
# left tcpreplay on the slower PF_PACKET send() path.
%make_build -C libopts CFLAGS="%{optflags} -std=gnu11"
%make_build

%install
%make_install

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
