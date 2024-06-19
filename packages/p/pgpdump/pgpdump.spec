#
# spec file for package pgpdump
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           pgpdump
Version:        0.36
Release:        0
Summary:        PGP packet visualizer
License:        BSD-3-Clause
URL:            https://www.mew.org/~kazu/proj/pgpdump/en/
Source:         https://www.mew.org/~kazu/proj/pgpdump/%{name}-%{version}.tar.gz

%description
pgpdump is a PGP packet visualizer which displays the packet format of OpenPGP
(RFC 4880) and PGP version 2 (RFC 1991).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
