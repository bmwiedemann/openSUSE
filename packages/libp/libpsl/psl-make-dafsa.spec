#
# spec file for package psl-make-dafsa
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2015 rpm@cicku.me
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


Name:           psl-make-dafsa
Version:        0.21.2
Release:        0
Summary:        Tool to create a binary DAFSA from a Public Suffix List
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://rockdaboot.github.io/libpsl
Source:         https://github.com/rockdaboot/libpsl/releases/download/%{version}/libpsl-%{version}.tar.gz
Requires:       python3-base
BuildArch:      noarch

%description
psl-make-dafsa converts ASCII string into C source or a binary format,
The format used is DAFSA, deterministic acyclic finate state automaton.

libpsl is capable of using this compact binary form of the Public Suffix List (PSL).

This package is a build dependency for the publicsuffix package.

%prep
%setup -q -n libpsl-%{version}
# fix env shebang to call py3 directly
sed -i -e "1s|#!.*|#!%{_bindir}/python3|" src/psl-make-dafsa

%build
:

%install
mkdir -p %{buildroot}%{_bindir}
install src/psl-make-dafsa %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 src/psl-make-dafsa.1 %{buildroot}%{_mandir}/man1

%files
%license src/LICENSE.chromium
%doc AUTHORS NEWS
%{_bindir}/psl-make-dafsa
%{_mandir}/man1/psl-make-dafsa.1%{?ext_man}

%changelog
