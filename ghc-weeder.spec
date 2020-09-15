#
# spec file for package ghc-weeder
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


%global pkg_name weeder
Name:           ghc-%{pkg_name}
Version:        2.1.1
Release:        0
Summary:        Detect dead code
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-algebraic-graphs-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-dhall-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel

%description
Find declarations.

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
sed -i -e 's#optparse-applicative \^>= 0\.14\.3\.0 || \^>= 0\.15\.1\.0#optparse-applicative < 1#' weeder.cabal
sed -i -e 's#dhall .* \^>= 1.33.0#dhall < 2#' weeder.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/%{pkg_name}

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
