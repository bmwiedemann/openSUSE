#
# spec file for package ghc-semigroupoids
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


%global pkg_name semigroupoids
Name:           ghc-%{pkg_name}
Version:        5.3.7
Release:        0
Summary:        Semigroupoids: Category sans id
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
ExcludeArch:    %{ix86}

%description
Provides a wide array of (semi)groupoids and operations for working with them.

A 'Semigroupoid' is a 'Category' without the requirement of identity arrows for
every object in the category.

A 'Category' is any 'Semigroupoid' for which the Yoneda lemma holds.

When working with comonads you often have the '<*>' portion of an
'Applicative', but not the 'pure'. This was captured in Uustalu and Vene's
"Essence of Dataflow Programming" in the form of the 'ComonadZip' class in the
days before 'Applicative'. Apply provides a weaker invariant, but for the
comonads used for data flow programming (found in the streams package), this
invariant is preserved. Applicative function composition forms a semigroupoid.

Similarly many structures are nearly a comonad, but not quite, for instance
lists provide a reasonable 'extend' operation in the form of 'tails', but do
not always contain a value.

We describe the relationships between the type classes defined in this package
and those from `base` (and some from `contravariant`) in the diagram below.
Thick-bordered nodes correspond to type classes defined in this package;
thin-bordered ones correspond to type classes from elsewhere. Solid edges
indicate a subclass relationship that actually exists; dashed edges indicate a
subclass relationship that /should/ exist, but currently doesn't.

<<https://raw.githubusercontent.com/ekmett/semigroupoids/master/img/classes.svg
Relationships among type classes from this package and others>>

Apply, Bind, and Extend (not shown) give rise the Static, Kleisli and Cokleisli
semigroupoids respectively.

This lets us remove many of the restrictions from various monad transformers as
in many cases the binding operation or '<*>' operation does not require them.

Finally, to work with these weaker structures it is beneficial to have
containers that can provide stronger guarantees about their contents, so
versions of 'Traversable' and 'Foldable' that can be folded with just a
'Semigroup' are added.

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
%doc CHANGELOG.markdown README.markdown

%changelog
