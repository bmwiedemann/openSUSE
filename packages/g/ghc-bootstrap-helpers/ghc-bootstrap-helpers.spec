#
# spec file for package ghc-bootstrap-helpers
#
# Copyright (c) 2019 SUSE LLC
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


Name:           ghc-bootstrap-helpers
Version:        1
Release:        0
Summary:        Dependencies to build ghc
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://build.opensuse.org/project/show/devel:languages:haskell
Source:         helpers.tar.gz
ExclusiveArch:  x86_64
Conflicts:      alex
Conflicts:      happy

%description
Prebuild alex and happy for ghc-8.8+ build

Don't use outside GHC-8.8+ build

%prep
%setup -q

%build

%install
cp -R * %{buildroot}/
rm -Rf %{buildroot}%{_datadir}/doc/*
rm -Rf %{buildroot}/usr/share/man/
rm -Rf %{buildroot}/usr/share/licenses/

%files
%{_bindir}/alex
%{_bindir}/happy
%dir %{_datadir}/happy-1.19.12/
%dir %{_datadir}/alex-3.2.5/
%{_datadir}/alex-3.2.5/*
%{_datadir}/happy-1.19.12/*

%changelog
