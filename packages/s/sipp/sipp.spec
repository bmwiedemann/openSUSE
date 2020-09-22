#
# spec file for package sipp
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


Name:           sipp
Version:        3.6.1
Release:        0
Summary:        A SIP protocol testing tool
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/SIPp/sipp
Source:         https://github.com/SIPp/sipp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
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
## FIXME: cmake oot-builds is broken
cp version.h src

%build
%cmake \
    -DUSE_GSL=1 \
    -DUSE_PCAP=1 \
    -DUSE_SSL=1 \
    -DUSE_SCTP=1
%make_build

%install
%cmake_install
## FIXME: manpage installation should be handled by cmake
install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license LICENSE.txt
%doc CHANGES.md README.md THANKS
%{_bindir}/%{name}
%{_mandir}/man1/sipp.1%{?ext_man}

%changelog
