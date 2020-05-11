#
# spec file for package ghc-lifted-async
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global pkg_name lifted-async
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.10.0.6
Release:        0
Summary:        Run lifted IO operations asynchronously and wait for their results
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-base-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-expected-failure-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-th-devel
%endif

%description
This package provides IO operations from 'async' package lifted to any instance
of 'MonadBase' or 'MonadBaseControl'.

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
%doc CHANGELOG.md README.md

%changelog
