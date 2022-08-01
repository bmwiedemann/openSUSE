#
# spec file for package ghc-monad-par
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


%global pkg_name monad-par
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.5
Release:        0
Summary:        A library for parallel programming based on a monad
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-abstract-deque-devel
BuildRequires:  ghc-abstract-par-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-monad-par-extras-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
BuildRequires:  ghc-test-framework-th-devel
BuildRequires:  ghc-time-devel
%endif

%description
The 'Par' monad offers a simple API for parallel programming. The library works
for parallelising both pure and 'IO' computations, although only the pure
version is deterministic. The default implementation provides a work-stealing
scheduler and supports forking tasks that are much lighter weight than
IO-threads.

For complete documentation see "Control.Monad.Par".

Some examples of use can be found in the 'examples/' directory of the source
package.

Other related packages:

* 'abstract-par' provides the type classes that abstract over different
implementations of the 'Par' monad.

* 'monad-par-extras' provides extra combinators and monad transformers layered
on top of the 'Par' monad.

Changes in 0.3.4 relative to 0.3:

* Fix bugs that cause "thread blocked indefinitely on MVar" crashes.

* Added "Control.Monad.Par.IO".

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

%changelog
