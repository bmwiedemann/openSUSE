#
# spec file for package ghc-hackage-security
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pkg_name hackage-security
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.6.4.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Hackage security library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-syntax-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-ed25519-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-zlib-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-Cabal-syntax-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptohash-sha256-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-ed25519-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-tar-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-zlib-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
%endif
%endif

%description
The hackage security library provides both server and client utilities for
securing the Hackage package server (<https://hackage.haskell.org/>).
It is based on The Update Framework (<https://theupdateframework.com/>), a set
of recommendations developed by security researchers at various universities in
the US as well as developers on the Tor project
(<https://www.torproject.org/>).

The current implementation supports only index signing, thereby enabling
untrusted mirrors. It does not yet provide facilities for author package
signing.

The library has two main entry points: "Hackage.Security.Client" is the main
entry point for clients (the typical example being 'cabal'), and
"Hackage.Security.Server" is the main entry point for servers (the typical
example being 'hackage-server').

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1 -n %pkg_name-%{version}

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
%doc ChangeLog.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
