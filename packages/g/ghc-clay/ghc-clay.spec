#
# spec file for package ghc-clay
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


%global pkg_name clay
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.13.3
Release:        0
Summary:        CSS preprocessor as embedded Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
%endif

%description
Clay is a CSS preprocessor like LESS and Sass, but implemented as an embedded
domain specific language (EDSL) in Haskell. This means that all CSS selectors
and style rules are first class Haskell functions, which makes reuse and
composability easy.

The project is described on <http://fvisser.nl/clay>.

The API documentation can be found in the top level module "Clay".

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
%doc CHANGELOG README.md

%changelog
