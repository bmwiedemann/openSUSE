#
# spec file for package ghc-persistent-sqlite
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


%global pkg_name persistent-sqlite
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.13.1.1
Release:        0
Summary:        Backend for the persistent library using sqlite3
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-resource-pool-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  glibc-devel
BuildRequires:  sqlite3-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-persistent-test-devel
BuildRequires:  ghc-system-fileio-devel
BuildRequires:  ghc-system-filepath-devel
BuildRequires:  ghc-temporary-devel
%endif

%description
This package includes a thin sqlite3 wrapper based on the direct-sqlite
package, as well as the entire C library, so there are no system dependencies.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       glibc-devel
Requires:       sqlite3-devel
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%define cabal_configure_options -fsystemlib
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
%doc ChangeLog.md

%changelog
