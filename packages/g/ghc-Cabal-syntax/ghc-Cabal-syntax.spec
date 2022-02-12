#
# spec file for package ghc-Cabal-syntax
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name Cabal-syntax
Name:           ghc-%{pkg_name}
Version:        3.6.0.0
Release:        0
Summary:        A library for working with .cabal files
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}

%description
This library provides tools for reading and manipulating the .cabal file
format.

Version 3.6 (unlike the following versions) is a dummy package that prevents
module name clases between Cabal and Cabal-syntax if used together with a Cabal
flag as described below.

In Cabal-3.7 this package was split off. To avoid module name clashes, you can
add this to your .cabal file:

> flag Cabal-syntax > description: Use the new Cabal-syntax package > default:
False > manual: False > > library > -- ... > if flag(Cabal-syntax) >
build-depends: Cabal-syntax >= 3.7 > else > build-depends: Cabal < 3.7,
Cabal-syntax < 3.7

This will default to the older build, but will allow consumers to opt-in to the
newer libraries by requiring Cabal or Cabal-syntax >= 3.7.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
