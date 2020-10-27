#
# spec file for package ghc-snap-core
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


%global pkg_name snap-core
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.0.4.2
Release:        0
Summary:        Snap: A Haskell Web Framework (core interfaces and types)
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-io-streams-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-readable-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
BuildRequires:  ghc-zlib-devel
%endif

%description
Snap is a simple and fast web development framework and server written in
Haskell. For more information or to download the latest version, you can visit
the Snap project website at <http://snapframework.com/>.

This library contains the core definitions and types for the Snap framework,
including:

1. Primitive types and functions for HTTP (requests, responses, cookies,
post/query parameters, etc)

2. A monad for programming web handlers called "Snap", which allows:

* Stateful access to the HTTP request and response objects

* Monadic failure (i.e. MonadPlus/Alternative instances) for declining to
handle requests and chaining handlers together

* Early termination of the computation if you know early what you want to
return and want to prevent further monadic processing

/Quick start/: The 'Snap' monad and HTTP definitions are in "Snap.Core".

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
%doc CONTRIBUTORS README.SNAP.md README.md

%changelog
