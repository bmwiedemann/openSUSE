#
# spec file for package ghc-base-noprelude
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


%global pkg_name base-noprelude
Name:           ghc-%{pkg_name}
Version:        4.13.0.0
Release:        0
Summary:        "base" package sans "Prelude" module
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
This package simplifies defining custom "Prelude"s without having to use
'-XNoImplicitPrelude' by re-exporting the full module-hierarchy of the
[base-4.13.0.0](https://hackage.haskell.org/package/base-4.13.0.0) package
/except/ for the "Prelude" module.

An usage example for such a "Prelude"-replacement is available with the
[Prelude](http://hackage.haskell.org/package/Prelude) package.

Starting with GHC 7.10 & Cabal-1.22 this package makes use of the package-level
'reexported-modules' feature.

Each version of 'base-noprelude' depends on a specific 'base'-version and thus
mirrors 'base''s versioning (with the exception that 'base-noprelude' needs to
add an /additional/ 5th version component in case of bug-fix releases).

See <https://github.com/hvr/base-noprelude> for more information.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}
cabal-tweak-dep-ver base '==4.13.0.0' '< 5'

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
