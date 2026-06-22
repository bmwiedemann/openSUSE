#
# spec file for package tiobench
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           tiobench
Version:        0.5.0
Release:        0
Summary:        Fully-threaded I/O benchmark program
License:        GPL-2.0-only
URL:            https://github.com/aliceinwire/tiobench
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Recommends:     perl(Term::ProgressBar)

%description
A simple multithreaded I/O benchmark, popular amongst kernel developers.
The results tend to be realistic enough to have some bearing on real
world results, while the tests are simple enough for kernel engineers to
analyze changes ...

%prep
%autosetup -p1
# avoid env-script-interpreter rpmlint error
sed -i '1s|/usr/bin/env perl|/usr/bin/perl|' tiobench.pl scripts/tiosum.pl

%build
%make_build CFLAGS="%{optflags} -fgnu89-inline"

%install
# upstream's "make install" target is broken (wrong tiosum.pl path), install manually
install -Dm0755 tiotest %{buildroot}%{_bindir}/tiotest
install -Dm0755 tiobench.pl %{buildroot}%{_bindir}/tiobench.pl
install -Dm0755 scripts/tiosum.pl %{buildroot}%{_bindir}/tiosum.pl

%files
%license COPYING
%doc ChangeLog README.md TODO
%{_bindir}/tio*

%changelog
