#
# spec file for package sipgrep
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%bcond_without redis
%bcond_without ncurses
%bcond_without compression
%bcond_without ssl
Name:           sipgrep
Version:        2.2.0
Release:        0
Summary:        Tool for displaying/troubleshooting SIP signaling on IP networks
License:        GPL-3.0-or-later
URL:            https://github.com/sipcapture/sipgrep
Source:         https://github.com/sipcapture/sipgrep/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         sipgrep-2.2.0-inet_pton.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpcre2-8)
%if %{with redis}
BuildRequires:  pkgconfig(hiredis)
%endif
%if %{with ncurses}
BuildRequires:  pkgconfig(ncurses)
%endif
%if %{with compression}
BuildRequires:  pkgconfig(zlib)
%endif
%if %{with ssl}
BuildRequires:  pkgconfig(libssl)
%endif

%description
Sipgrep is a pcap-aware tool command line tool to sniff, capture,
display and troubleshoot SIP signaling over IP networks. The user can
specify extended regular expressions matching against SIP headers.

%prep
%autosetup -p1

%build
# the versioned configure script still looks for pcre
autoreconf -fiv
%configure \
	--enable-ipv6 \
%if %{with redis}
	--enable-redis \
%endif
%if %{with ncurses}
	--enable-ncurses \
%endif
%if %{with compression}
	--enable-compression \
%endif
%if %{with ssl}
	--enable-ssl \
%endif
	%{nil}
%make_build

%install
%make_install
install -D -m0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%check
%make_build check

%files
%license COPYING
%doc README.md
%{_bindir}/sipgrep
%{_mandir}/man8/sipgrep.8%{?ext_man}

%changelog
