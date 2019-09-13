#
# spec file for package mcjoin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mcjoin
Version:        2.3
Release:        0
Summary:        IPv4 tool for verifying multicast connectivity
License:        ISC
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/troglobit/mcjoin
#Git-Clone:     https://github.com/troglobit/mcjoin.git
Source:         https://github.com/troglobit/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake

%description
mcjoin can be used to join IPv4 multicast groups, display
progress as multicast packets are received, and also send
multicast packets on select groups.

mcjoin can help verify intended IGMP snooping functionality
in layer-2 bridges/switches, as well as test forwarding of
multicast in static or dynamic multicast routing setups.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc

%files
%license LICENSE
%doc AUTHORS ChangeLog.md README.md
%{_bindir}/mcjoin
%{_mandir}/man1/mcjoin.1%{?ext_man}

%changelog
