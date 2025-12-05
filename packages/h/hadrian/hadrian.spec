#
# spec file for package hadrian
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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

%global ghc_ver 9.12.2

Name:           hadrian
Version:        0.1.0.0
Release:        0
Summary:        GHC Hadrian buildsystem tool 
License:        BSD-3-Clause
URL:            https://gitlab.haskell.org/ghc/ghc
Source:         ghc-%{ghc_ver}-src.tar.xz 
Source1:        9_10_1-bootstrap-sources.tar.gz 
BuildRequires:  ghc-bootstrap
BuildRequires:  python3
# This package is not meant to be used outside OBS
#Requires:       this-is-only-for-build-envs

%description
This provides the hadrian tool used to build ghc.

%prep
%setup -n ghc-%{ghc_ver}

%build
cp %{SOURCE1} ./
hadrian/bootstrap/bootstrap.py --bootstrap-sources 9_10_1-bootstrap-sources.tar.gz

%install
echo $PWD
ls -al
install -d %{buildroot}%{_bindir}
install -p _build/bin/hadrian %{buildroot}%{_bindir}/hadrian


%files
%license LICENSE
%doc README.md
%{_bindir}/hadrian

%changelog
