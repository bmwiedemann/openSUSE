#
# spec file for package ghc-hspec-core
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


%global pkg_name hspec-core
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.7.4
Release:        0
Summary:        A Testing Framework for Haskell
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-quickcheck-io-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-setenv-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tf-random-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-hspec-meta-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-temporary-devel
%endif

%description
This package exposes internal types and functions that can be used to extend
Hspec's functionality.

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
