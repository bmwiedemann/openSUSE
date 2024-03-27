#
# spec file for package ghc-bootstrap-helpers
#
# Copyright (c) 2023 SUSE LLC
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


%define         alex_ver 3.5.1.0
%define         happy_ver 1.20.1.1

Name:           ghc-bootstrap-helpers
Version:        1.4
Release:        0
Summary:        Dependencies to build ghc
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://build.opensuse.org/project/show/devel:languages:haskell
Source:         https://hackage.haskell.org/package/alex-%{alex_ver}/alex-%{alex_ver}.tar.gz
Source1:        https://hackage.haskell.org/package/happy-%{happy_ver}/happy-%{happy_ver}.tar.gz
BuildRequires:  ghc-bootstrap
ExcludeArch:    %{ix86}
# This package is not meant to be used outside OBS
Requires:       this-is-only-for-build-envs

Conflicts:      alex
Conflicts:      happy

%description
Prebuild alex and happy for bootstrapping the proper ghc build.
Don't use outside of GHC bootstrapping!

%prep
%setup -q -c -a0 -a1

%build
pushd alex-%{alex_ver}
/opt/bin/ghc Setup.hs -o cabal
./cabal configure --prefix=%{_prefix}
./cabal build
popd

pushd happy-%{happy_ver}
/opt/bin/ghc Setup.hs -o cabal
./cabal configure --prefix=%{_prefix}
./cabal build
popd

%install
pushd alex-%{alex_ver}
./cabal copy --destdir=%{buildroot}
popd

pushd happy-%{happy_ver}
./cabal copy --destdir=%{buildroot}
popd

%files
%{_bindir}/alex
%{_bindir}/happy
%{_datadir}/*ghc*
%{_datadir}/doc/*ghc*

%changelog
