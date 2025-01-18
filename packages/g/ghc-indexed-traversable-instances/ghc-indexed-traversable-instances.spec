#
# spec file for package ghc-indexed-traversable-instances
#
# Copyright (c) 2025 SUSE LLC
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


%global pkg_name indexed-traversable-instances
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.2
Release:        0
Summary:        More instances of FunctorWithIndex, FoldableWithIndex, TraversableWithIndex
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-OneTuple-devel
BuildRequires:  ghc-OneTuple-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-quickcheck-instances-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
%endif

%description
This package provides extra instances for type-classes in the
[indexed-traversable](https://hackage.haskell.org/package/indexed-traversable)
package.

The intention is to keep this package minimal; it provides instances that
formely existed in 'lens' or 'optics-extra'. We recommend putting other
instances directly into their defining packages. The 'indexed-traversable'
package is light, having only GHC boot libraries as its dependencies.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library
development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

%prep
%autosetup -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%doc Changelog.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
