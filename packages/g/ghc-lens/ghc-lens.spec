#
# spec file for package ghc-lens
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name lens
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        5.3.3
Release:        0
Summary:        Lenses, Folds and Traversals
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-assoc-devel
BuildRequires:  ghc-assoc-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-call-stack-prof
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-distributive-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-free-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-indexed-traversable-instances-devel
BuildRequires:  ghc-indexed-traversable-instances-prof
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-kan-extensions-devel
BuildRequires:  ghc-kan-extensions-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-parallel-prof
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-reflection-devel
BuildRequires:  ghc-reflection-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-strict-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-simple-reflect-devel
BuildRequires:  ghc-simple-reflect-prof
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-hunit-prof
BuildRequires:  ghc-test-framework-prof
BuildRequires:  ghc-test-framework-quickcheck2-devel
BuildRequires:  ghc-test-framework-quickcheck2-prof
%endif

%description
This package comes "Batteries Included" with many useful lenses for the types
commonly used from the Haskell Platform, and with tools for automatically
generating lenses and isomorphisms for user-supplied data types.

The combinators in 'Control.Lens' provide a highly generic toolbox for
composing families of getters, folds, isomorphisms, traversals, setters and
lenses and their indexed variants.

An overview, with a large number of examples can be found in the
<https://github.com/ekmett/lens#lens-lenses-folds-and-traversals README>.

An introductory video on the style of code used in this library by Simon Peyton
Jones is available from
<https://archive.org/details/lenses-compositional-data-access-and-manipulation-simon-peyton-jones-at-haskell-
Internet Archive>.

A video on how to use lenses and how they are constructed is available on
<http://youtu.be/cefnmjtAolY?hd=1 youtube>.

Slides for that second talk can be obtained from
<http://comonad.com/haskell/Lenses-Folds-and-Traversals-NYC.pdf comonad.com>.

More information on the care and feeding of lenses, including a brief tutorial
and motivation for their types can be found on the
<https://github.com/ekmett/lens/wiki lens wiki>.

A small game of 'pong' and other more complex examples that manage their state
using lenses can be found in the
<https://github.com/ekmett/lens/blob/master/examples/ example folder>.

/Lenses, Folds and Traversals/

With some signatures simplified, the core of the hierarchy of lens-like
constructions looks like:

<<http://i.imgur.com/ALlbPRa.png>>

<https://raw.githubusercontent.com/ekmett/lens/master/images/Hierarchy.png
(Local Copy)>

You can compose any two elements of the hierarchy above using '(.)' from the
'Prelude', and you can use any element of the hierarchy as any type it linked
to above it.

The result is their lowest upper bound in the hierarchy (or an error if that
bound doesn't exist).

For instance:

* You can use any 'Traversal' as a 'Fold' or as a 'Setter'.

* The composition of a 'Traversal' and a 'Getter' yields a 'Fold'.

/Minimizing Dependencies/

If you want to provide lenses and traversals for your own types in your own
libraries, then you can do so without incurring a dependency on this (or any
other) lens package at all.

/e.g./ for a data type:

> data Foo a = Foo Int Int a

You can define lenses such as

> -- bar :: Lens' (Foo a) Int > bar :: Functor f => (Int -> f Int) -> Foo a ->
f (Foo a) > bar f (Foo a b c) = fmap (a' -> Foo a' b c) (f a)

> -- quux :: Lens (Foo a) (Foo b) a b > quux :: Functor f => (a -> f b) -> Foo
a -> f (Foo b) > quux f (Foo a b c) = fmap (Foo a b) (f c)

without the need to use any type that isn't already defined in the 'Prelude'.

And you can define a traversal of multiple fields with
'Control.Applicative.Applicative':

> -- traverseBarAndBaz :: Traversal' (Foo a) Int > traverseBarAndBaz ::
Applicative f => (Int -> f Int) -> Foo a -> f (Foo a) > traverseBarAndBaz f
(Foo a b c) = Foo <$> f a <*> f b <*> pure c

What is provided in this library is a number of stock lenses and traversals for
common haskell types, a wide array of combinators for working them, and more
exotic functionality, (/e.g./ getters, setters, indexed folds, isomorphisms).

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

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
%doc AUTHORS.markdown CHANGELOG.markdown README.markdown examples

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
