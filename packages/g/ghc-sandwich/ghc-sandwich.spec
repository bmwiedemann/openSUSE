#
# spec file for package ghc-sandwich
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name sandwich
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.2.0
Release:        0
Summary:        Yet another test framework for Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-brick-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-lifted-async-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-string-interpolate-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vty-devel
ExcludeArch:    %{ix86}

%description
Please see the <https://codedownio.github.io/sandwich documentation>.

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
%{_bindir}/sandwich-demo
%{_bindir}/sandwich-discover
%{_bindir}/sandwich-test

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
