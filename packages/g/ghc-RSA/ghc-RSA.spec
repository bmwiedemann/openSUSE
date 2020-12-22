#
# spec file for package ghc-RSA
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


%global pkg_name RSA
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.4.1
Release:        0
Summary:        Implementation of RSA, using the padding schemes of PKCS#1 v2.1
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-crypto-pubkey-types-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
This library implements the RSA encryption and signature algorithms for
arbitrarily-sized ByteStrings. While the implementations work, they are not
necessarily the fastest ones on the planet. Particularly key generation.
The algorithms included are based of RFC 3447, or the Public-Key Cryptography
Standard for RSA, version 2.1 (a.k.a, PKCS#1 v2.1).

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

%changelog
