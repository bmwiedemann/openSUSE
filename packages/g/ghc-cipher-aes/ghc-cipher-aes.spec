#
# spec file for package ghc-cipher-aes
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


%global pkg_name cipher-aes
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.11
Release:        0
Summary:        Fast AES cipher implementation with advanced mode of operations
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-crypto-cipher-types-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-securemem-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-crypto-cipher-tests-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
Fast AES cipher implementation with advanced mode of operations.

The modes of operations available are ECB (Electronic code book), CBC (Cipher
block chaining), CTR (Counter), XTS (XEX with ciphertext stealing), GCM (Galois
Counter Mode).

The AES implementation uses AES-NI when available (on x86 and x86-64
architecture), but fallback gracefully to a software C implementation.

The software implementation uses S-Boxes, which might suffer for cache timing
issues. However do notes that most other known software implementations,
including very popular one (openssl, gnutls) also uses similar implementation.
If it matters for your case, you should make sure you have AES-NI available, or
you'll need to use a different implementation.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}

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
