#
# spec file for package mcjoin
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           mcjoin
Version:        2.12
Release:        0
Summary:        IPv4 tool for verifying multicast connectivity
License:        ISC
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/troglobit/mcjoin
#Git-Clone:     https://github.com/troglobit/mcjoin.git
Source:         https://github.com/troglobit/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

%description
mcjoin can be used to join IPv4 multicast groups, display
progress as multicast packets are received, and also send
multicast packets on select groups.

mcjoin can help verify intended IGMP snooping functionality
in layer-2 bridges/switches, as well as test forwarding of
multicast in static or dynamic multicast routing setups.

%prep
%autosetup -p1

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install
# installed via macro
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%check
%make_build check

%files
%license LICENSE
%doc ChangeLog.md
%doc %{_docdir}/%{name}
%{_bindir}/mcjoin
%{_mandir}/man1/mcjoin.1%{?ext_man}

%changelog
