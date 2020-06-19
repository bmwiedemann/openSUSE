#
# spec file for package ghc-tls
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


%global pkg_name tls
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.5.4
Release:        0
Summary:        TLS/SSL protocol native implementation (Server and Client)
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-asn1-encoding-devel
BuildRequires:  ghc-asn1-types-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-hourglass-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-x509-devel
BuildRequires:  ghc-x509-store-devel
BuildRequires:  ghc-x509-validation-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Native Haskell TLS and SSL protocol implementation for server and client.

This provides a high-level implementation of a sensitive security protocol,
eliminating a common set of security issues through the use of the advanced
type system, high level constructions and common Haskell features.

Currently implement the SSL3.0, TLS1.0, TLS1.1, TLS1.2 and TLS 1.3 protocol,
and support RSA and Ephemeral (Elliptic curve and regular) Diffie Hellman key
exchanges, and many extensions.

Some debug tools linked with tls, are available through the
<http://hackage.haskell.org/package/tls-debug/>.

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
%doc CHANGELOG.md

%changelog
