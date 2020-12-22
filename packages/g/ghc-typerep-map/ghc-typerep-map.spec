#
# spec file for package ghc-typerep-map
#
# Copyright (c) 2020 SUSE LLC
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


%global pkg_name typerep-map
%global has_internal_sub_libraries 1
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.3.0
Release:        0
Summary:        Efficient implementation of a dependent map with types as keys
License:        MPL-2.0
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-ghc-typelits-knownnat-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-hedgehog-devel
%endif

%description
A dependent map from type representations to values of these types.

Here is an illustration of such a map:

> TMap > --------------- > Int -> 5 > Bool -> True > Char -> 'x'

In addition to 'TMap', we provide 'TypeRepMap' parametrized by a 'vinyl'-style
interpretation. This data structure is equivalent to 'DMap TypeRep', but with
significantly more efficient lookups.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build_without_haddock

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
