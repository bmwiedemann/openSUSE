#
# spec file for package deal
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


Name:           deal
Version:        2.7
Release:        0
Summary:        Calculator for nonreplacement probabilities
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/deal/
Source:         http://www.catb.org/~esr/deal/%{name}-%{version}.tar.gz

%description
This program computes odd for drawing card sets (e.g. non-replacement
probabilities) using the hypergeometric function. It can also be used to
compute binomial coefficients and the gamma function.

%prep
%autosetup -p1

%build
%make_build

%install
# makefile is awfully broken
install -D deal %{buildroot}%{_bindir}/deal
install -D -m 644 deal.1 %{buildroot}%{_mandir}/man1/deal.1

%check
%{buildroot}%{_bindir}/deal 3 62
%{buildroot}%{_bindir}/deal -b 5 4 52

%files
%license COPYING
%doc NEWS.adoc README.adoc
%{_bindir}/deal
%{_mandir}/man1/deal.1%{?ext_man}

%changelog
