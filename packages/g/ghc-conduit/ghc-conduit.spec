#
# spec file for package ghc-conduit
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


%global pkg_name conduit
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.3.2.1
Release:        0
Summary:        Streaming data processing library
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mono-traversable-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-unliftio-devel
%endif

%description
`conduit` is a solution to the streaming data problem, allowing for production,
transformation, and consumption of streams of data in constant memory.
It is an alternative to lazy I/O which guarantees deterministic resource
handling.

For more information about conduit in general, and how this package in
particular fits into the ecosystem, see [the conduit
homepage](https://github.com/snoyberg/conduit#readme).

Hackage documentation generation is not reliable. For up to date documentation,
please see: <http://www.stackage.org/package/conduit>.

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
%doc ChangeLog.md README.md

%changelog
