#
# spec file for package ghc-free
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


%global pkg_name free
Name:           ghc-%{pkg_name}
Version:        5.1.4
Release:        0
Summary:        Monads for free
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel

%description
Free monads are useful for many tree-like structures and domain specific
languages.

If 'f' is a 'Functor' then the free 'Monad' on 'f' is the type of trees whose
nodes are labeled with the constructors of 'f'. The word "free" is used in the
sense of "unrestricted" rather than "zero-cost": 'Free f' makes no constraining
assumptions beyond those given by 'f' and the definition of 'Monad'.
As used here it is a standard term from the mathematical theory of adjoint
functors.

Cofree comonads are dual to free monads. They provide convenient ways to talk
about branching streams and rose-trees, and can be used to annotate syntax
trees. The cofree comonad can be seen as a stream parameterized by a 'Functor'
that controls its branching factor.

More information on free monads, including examples, can be found in the
following blog posts: <http://comonad.com/reader/2008/monads-for-free/>
<http://comonad.com/reader/2011/free-monads-for-less/>.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown doc examples

%changelog
