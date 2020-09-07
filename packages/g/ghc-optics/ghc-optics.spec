#
# spec file for package ghc-optics
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


%global pkg_name optics
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3
Release:        0
Summary:        Optics as an abstract interface
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optics-core-devel
BuildRequires:  ghc-optics-extra-devel
BuildRequires:  ghc-optics-th-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-indexed-profunctors-devel
BuildRequires:  ghc-inspection-testing-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-template-haskell-devel
%endif

%description
This package makes it possible to define and use Lenses, Traversals, Prisms and
other optics, using an abstract interface. See the main module "Optics" for the
documentation.

This is the "batteries-included" variant with many dependencies; see the
'<https://hackage.haskell.org/package/optics-core optics-core>' package and
other 'optics-*' dependencies if you need a more limited dependency footprint.

Note: Hackage does not yet display documentation for reexported-modules, but
you can start from the "Optics" module documentation or see the module list in
'<https://hackage.haskell.org/package/optics-core optics-core>'.

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
%ghc_lib_build

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
%doc CHANGELOG.md

%changelog
