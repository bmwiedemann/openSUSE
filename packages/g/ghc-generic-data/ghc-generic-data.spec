#
# spec file for package ghc-generic-data
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


%global pkg_name generic-data
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.0.0.0
Release:        0
Summary:        Deriving instances with GHC.Generics and related utilities
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ap-normalize-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-ghc-boot-th-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-show-combinators-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-one-liner-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif

%description
Generic implementations of standard type classes. Operations on generic
representations to help using "GHC.Generics". See README.

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
%doc CHANGELOG.md README.md

%changelog
