#
# spec file for package ghc-vector-builder
#
# Copyright (c) 2019 SUSE LLC
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


%global pkg_name vector-builder
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.8
Release:        0
Summary:        Vector builder
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-prelude-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-rerebase-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
An API for efficient and convenient construction of vectors. It provides the
composable `Builder` abstraction, which has instances of the `Monoid` and
`Semigroup` classes.

[Usage]

First you use the `Builder` abstraction to specify the structure of the vector.
Then you execute the builder to actually produce the vector.

[Example]

The following code shows how you can efficiently concatenate different
datastructures into a single immutable vector:

> >import qualified Data.Vector as A >import qualified VectorBuilder.Builder as
B >import qualified VectorBuilder.Vector as C > > >myVector :: A.Vector a ->
[a] -> a -> A.Vector a >myVector vector list element = > C.build builder >
where > builder = > B.vector vector <> > B.foldable list <> > B.singleton
element.

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

%changelog
