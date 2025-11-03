#
# spec file for package letterize
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


Name:           letterize
Version:        1.5
Release:        0
Summary:        Find pronounceable letter mnemonics for phone numbers
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/letterize/
Source:         http://www.catb.org/~esr/letterize/%{name}-%{version}.tar.gz

%description
This program uses a table of pronounceable letter-triples derived from a
dictionary scan. Each potential mnemonic must be such that all of its
letter-triples are in the table to be emitted. About 30% of possible triples
are considered pronounceable. A typical 7-digit phone number has 19,683
possible mnemonics, but this test usually cuts the list down to a few hundred
or so, a reasonable number to eyeball-check. For some numbers, the list will,
sadly, be empty.

%prep
%autosetup -p1

%build
%make_build

%install
# makefile is awfully broken
install -D letterize %{buildroot}%{_bindir}/letterize
install -D -m 644 letterize.1 %{buildroot}%{_mandir}/man1/letterize.1

%check
%{buildroot}%{_bindir}/%{name} 42

%files
%license COPYING
%doc NEWS README
%{_bindir}/letterize
%{_mandir}/man1/letterize.1%{?ext_man}

%changelog
