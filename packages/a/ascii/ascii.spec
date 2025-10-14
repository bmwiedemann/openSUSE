#
# spec file for package ascii
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


Name:           ascii
Version:        3.30
Release:        0
Summary:        List ASCII idiomatic names and octal/decimal code-point form
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/ascii/
Source:         http://www.catb.org/~esr/ascii/%{name}-%{version}.tar.gz
Source2:        ascii-rpmlintrc

%description
Provides easy conversion between various byte representations and the American
Standard Code for Information Interchange (ASCII) character table. It knows
about a wide variety of hex, binary, octal, Teletype mnemonic, ISO/ECMA code
point, slang names, XML entity names, and other representations. Given any one
on the command line, it will try to display all others. Called with no
arguments it displays a handy small ASCII chart.

%prep
%autosetup -p1

%build
%make_build ascii ascii.1 CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%make_build install \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	%{nil}

%check
%{buildroot}%{_bindir}/ascii

%files
%license COPYING
%doc NEWS.adoc README
%{_bindir}/ascii
%{_mandir}/man1/ascii.1%{?ext_man}

%changelog
