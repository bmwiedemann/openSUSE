#
# spec file for package ghc-data-array-byte
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


%global pkg_name data-array-byte
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.0.1
Release:        0
Summary:        Compatibility layer for Data.Array.Byte
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-quickcheck-classes-base-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Compatibility layer for
[Data.Array.Byte](https://hackage.haskell.org/package/base/docs/Data-Array-Byte.html),
providing boxed wrappers for 'ByteArray#' and 'MutableByteArray#' and relevant
instances for GHC < 9.4. Include it into your Cabal file:

> build-depends: base > if impl(ghc < 9.4) > build-depends: data-array-byte

and then 'import Data.Array.Byte' unconditionally.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%doc README.md changelog.md

%changelog
