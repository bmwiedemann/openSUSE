#
# spec file for package ghc-async
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global pkg_name async
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.2.2
Release:        0
Summary:        Run IO operations asynchronously and wait for their results
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
%endif

%description
This package provides a higher-level interface over threads, in which an 'Async
a' is a concurrent thread that will eventually deliver a value of type 'a'.
The package provides ways to create 'Async' computations, wait for their
results, and cancel them.

Using 'Async' is safer than using threads in two ways:

* When waiting for a thread to return a result, if the thread dies with an
exception then the caller must either re-throw the exception ('wait') or handle
it ('waitCatch'); the exception cannot be ignored.

* The API makes it possible to build a tree of threads that are automatically
killed when their parent dies (see 'withAsync').

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

%files devel -f %{name}-devel.files
%doc changelog.md

%changelog
