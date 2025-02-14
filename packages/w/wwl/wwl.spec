#
# spec file for package wwl
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


Name:           wwl
Version:        1.3
Release:        0
Summary:        Calculates distance (qrb) used in Amateur Radio
# From wwl.c: # [...] As long as you retain this notice you
# can do whatever you want with this code, except you may not
# license it under any form of the GPL.
License:        SUSE-Freeware
URL:            http://www.db.net/downloads/
Source:         http://www.db.net/downloads/wwl+db-%{version}.tgz
Source2:        LICENSE

%description
Given two Maidenhead locators, calculates distance (qrb) and azimuth
Or if called as locator, gives the lat/long of a Maidenhead locator.

%prep
%autosetup -p1 -n %{name}+db-%{version}
cp %{SOURCE2} .

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%make_install \
	PREFIX=%{buildroot}%{_prefix} \
	MAN1PREFIX=%{buildroot}%{_mandir}/man1/ \
	LN="ln -r" \
	%{nil}
chmod -x %{buildroot}%{_mandir}/man1/wwl.1*

%files
%license LICENSE
%{_bindir}/locator
%{_bindir}/wwl
%{_mandir}/man1/locator.1%{?ext_man}
%{_mandir}/man1/wwl.1%{?ext_man}

%changelog
