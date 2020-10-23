#
# spec file for package ghc-lens
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


%global pkg_name lens
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        4.19.2
Release:        0
Summary:        Lenses, Folds and Traversals
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cabal-doctest-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-kan-extensions-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-reflection-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-nats-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-simple-reflect-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
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
<http://skillsmatter.com/podcast/scala/lenses-compositional-data-access-and-manipulation
Skills Matter>.

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

<images/Hierarchy.png (Local Copy)>

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
%doc AUTHORS.markdown CHANGELOG.markdown README.markdown examples

%changelog
