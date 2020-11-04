#
# spec file for package ghc-generic-deriving
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


%global pkg_name generic-deriving
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.14
Release:        0
Summary:        Generic programming library for generalised deriving
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-abstraction-devel
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%endif

%description
This package provides functionality for generalising the deriving mechanism in
Haskell to arbitrary classes. It was first described in the paper:

* /A generic deriving mechanism for Haskell/. Jose Pedro Magalhaes, Atze
Dijkstra, Johan Jeuring, and Andres Loeh. Haskell'10.

The current implementation integrates with the new GHC Generics. See
<http://www.haskell.org/haskellwiki/GHC.Generics> for more information.
Template Haskell code is provided for supporting older GHCs.

This library is organized as follows:

* "Generics.Deriving.Base" defines the core functionality for GHC generics,
including the 'Generic(1)' classes and representation data types. On modern
versions of GHC, this simply re-exports "GHC.Generics" from 'base'. On older
versions of GHC, this module backports parts of "GHC.Generics" that were not
included at the time, including 'Generic(1)' instances.

* "Generics.Deriving.TH" implements Template Haskell functionality for deriving
instances of 'Generic(1)'.

* Educational code: in order to provide examples of how to define and use
"GHC.Generics"-based defaults, this library offers a number of modules which
define examples of type classes along with default implementations for the
classes' methods. Currently, the following modules are provided:
"Generics.Deriving.Copoint", "Generics.Deriving.ConNames",
"Generics.Deriving.Enum", "Generics.Deriving.Eq", "Generics.Deriving.Foldable",
"Generics.Deriving.Functor", "Generics.Deriving.Monoid",
"Generics.Deriving.Semigroup", "Generics.Deriving.Show",
"Generics.Deriving.Traversable", and "Generics.Deriving.Uniplate".

It is worth emphasizing that these modules are primarly intended for
educational purposes. Many of the classes in these modules resemble other
commonly used classes—for example, 'GShow' from "Generics.Deriving.Show"
resembles 'Show' from 'base'—but in general, the classes that
'generic-deriving' defines are not drop-in replacements. Moreover, the generic
defaults that 'generic-deriving' provide often make simplifying assumptions
that may violate expectations of how these classes might work elsewhere.
For example, the generic default for 'GShow' does not behave exactly like
'deriving Show' would.

If you are seeking "GHC.Generics"-based defaults for type classes in 'base',
consider using the '<http://hackage.haskell.org/package/generic-data
generic-data>' library.

* "Generics.Deriving.Default" provides newtypes that allow leveraging the
generic defaults in this library using the 'DerivingVia' GHC language
extension.

* "Generics.Deriving" re-exports "Generics.Deriving.Base",
"Generics.Deriving.Default", and a selection of educational modules.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%doc CHANGELOG.md README.md

%changelog
