#
# spec file for package sngrep
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           sngrep
Version:        1.4.7
Release:        0
Summary:        Ncurses SIP Messages flow viewer
License:        GPL-3.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://github.com/irontec/sngrep
#Git-Clone:     https://github.com/irontec/sngrep.git
Source:         https://github.com/irontec/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-build-with-recent-ncurses-versions.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(ncursesw)

%description
sngrep displays SIP Messages grouped by Call-Id into flow
diagrams. It can be used as an offline pcap viewer or online
capture using libpcap functions.

It supports SIP UDP and TCP transports (when each message is
delivered in one packet).

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
export CFLAGS="%optflags $(pkg-config --cflags ncursesw)"
%configure \
    --enable-unicode \
    --with-openssl \
    --with-pcre \
    --enable-ipv6 \
    --enable-eep

make V=1 %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc AUTHORS README.md
%config %{_sysconfdir}/sngreprc
%{_bindir}/sngrep
%{_mandir}/man8/sngrep.8%{ext_man}

%changelog
