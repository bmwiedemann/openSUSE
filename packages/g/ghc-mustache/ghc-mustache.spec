#
# spec file for package ghc-mustache
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


%global pkg_name mustache
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.3.1
Release:        0
Summary:        A mustache template parser library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
%if %{with tests}
BuildRequires:  ghc-base-unicode-symbols-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-wreq-devel
BuildRequires:  ghc-zlib-devel
%endif

%description
Allows parsing and rendering template files with mustache markup. See the
mustache <http://mustache.github.io/mustache.5.html language reference>.

Implements the mustache spec version 1.1.3.

/Note/: Versions including and beyond 0.4 are compatible with ghc 7.8 again.

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
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/haskell-mustache

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
