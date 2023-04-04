#
# spec file for package ghc-resolv
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


%global pkg_name resolv
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.2.0
Release:        0
Summary:        Domain Name Service (DNS) lookup via the libresolv standard library routines
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/6.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
%endif

%description
This package implements an API for accessing the [Domain Name Service
(DNS)](https://tools.ietf.org/html/rfc1035) resolver service via the standard
'libresolv' system library (whose API is often available directly via the
standard 'libc' C library) on Unix systems.

This package also includes support for decoding message record types as defined
in the following RFCs:

- [RFC 1035](https://tools.ietf.org/html/rfc1035): Domain Names -
Implementation And Specification - [RFC
1183](https://tools.ietf.org/html/rfc1183): New DNS RR Definitions - [RFC
2782](https://tools.ietf.org/html/rfc2782): A DNS RR for specifying the
location of services (DNS SRV) - [RFC
2915](https://tools.ietf.org/html/rfc2915): The Naming Authority Pointer
(NAPTR) DNS Resource Record - [RFC 3596](https://tools.ietf.org/html/rfc3596):
DNS Extensions to Support IP Version 6 - [RFC
4034](https://tools.ietf.org/html/rfc4034): Resource Records for the DNS
Security Extensions - [RFC 4255](https://tools.ietf.org/html/rfc4255): Using
DNS to Securely Publish Secure Shell (SSH) Key Fingerprints - [RFC
4408](https://tools.ietf.org/html/rfc4408): Sender Policy Framework (SPF) for
Authorizing Use of Domains in E-Mail, Version 1 - [RFC
5155](https://tools.ietf.org/html/rfc5155): DNS Security (DNSSEC) Hashed
Authenticated Denial of Existence - [RFC
6844](https://tools.ietf.org/html/rfc6844): DNS Certification Authority
Authorization (CAA) Resource Record - [RFC
6891](https://tools.ietf.org/html/rfc6891): Extension Mechanisms for DNS
(EDNS(0)) - [RFC 7553](https://tools.ietf.org/html/rfc7553): The Uniform
Resource Identifier (URI) DNS Resource Record

For Windows, the package [windns](https://hackage.haskell.org/package/windns)
provides a compatible subset of this package's API.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

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
%license LICENSE.GPLv2
%license LICENSE.GPLv3

%files devel -f %{name}-devel.files
%doc ChangeLog.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE
%license LICENSE.GPLv2
%license LICENSE.GPLv3

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
