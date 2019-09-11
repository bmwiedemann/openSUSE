#
# spec file for package flawfinder
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


Name:           flawfinder
Version:        2.0.10
Release:        0
Summary:        C/C++ source code security flaw examination tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://www.dwheeler.com/flawfinder/
Source:         http://www.dwheeler.com/flawfinder/%{name}-%{version}.tar.gz
Requires:       python3
BuildArch:      noarch

%description
Flawfinder scans through C/C++ source code, identifying lines
("hits") with potential security flaws. By default it reports hits
sorted by severity, with the riskiest lines first.

%prep
%setup -q
sed -i "s|!/usr/bin/env python|!/usr/bin/python3|" flawfinder
chmod -x *.ps

%build
make %{?_smp_mflags}

%install
install -m755 -D flawfinder %{buildroot}%{_bindir}/flawfinder
install -m644 -D flawfinder.1 %{buildroot}%{_mandir}/man1/flawfinder.1

%files
%license COPYING
%doc README.md ChangeLog flawfinder.ps
%{_bindir}/flawfinder
%{_mandir}/man1/flawfinder.1%{?ext_man}

%changelog
