#
# spec file for package sipp
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


Name:           sipp
Version:        3.6.0
Release:        0
Summary:        A SIP protocol testing tool
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/SIPp/sipp
Source:         https://github.com/SIPp/sipp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libpcap-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libssl)

%description
Sipp is a performance testing tool for the SIP protocol. Its main features are
basic SIPStone scenarios, TCP/UDP transport, customizable (xml based) scenarios,
dynamic adjustement of call-rate and a comprehensive set of real-time
statistics.

%prep
%setup -q

%build
autoreconf -fiv
%configure --with-pcap --with-sctp --with-openssl --with-gsl --with-rtpstream
make %{?_smp_mflags}

%install
%make_install

%files
%doc CHANGES.md README.md THANKS
%license LICENSE.txt
%{_bindir}/%{name}
%{_mandir}/man1/sipp.1%{?ext_man}

%changelog
