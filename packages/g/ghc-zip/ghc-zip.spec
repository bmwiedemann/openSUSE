#
# spec file for package ghc-zip
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


%global pkg_name zip
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.7.2
Release:        0
Summary:        Operations on zip archives
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/3.cabal#/%{pkg_name}.cabal
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bzlib-conduit-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-conduit-zstd-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-temporary-devel
%endif

%description
Operations on zip archives.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE.md
%{_bindir}/haskell-zip-app

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
