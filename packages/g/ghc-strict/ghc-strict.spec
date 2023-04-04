#
# spec file for package ghc-strict
#
# Copyright (c) 2023 SUSE LLC
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


%global pkg_name strict
%global pkgver %{pkg_name}-%{version}
Name:           ghc-%{pkg_name}
Version:        0.4.0.1
Release:        0
Summary:        Strict data types and String IO
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/4.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-assoc-devel
BuildRequires:  ghc-assoc-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
ExcludeArch:    %{ix86}

%description
This package provides strict versions of some standard Haskell data types
(pairs, Maybe and Either). It also contains strict IO operations.

It is common knowledge that lazy datastructures can lead to space-leaks.
This problem is particularly prominent, when using lazy datastructures to store
the state of a long-running application in memory. One common solution to this
problem is to use 'seq' and its variants in every piece of code that updates
your state. However a much easier solution is to use fully strict types to
store such state values. By "fully strict types" we mean types for whose values
it holds that, if they are in weak-head normal form, then they are also in
normal form. Intuitively, this means that values of fully strict types cannot
contain unevaluated thunks.

To define a fully strict datatype, one typically uses the following recipe.

1. Make all fields of every constructor strict; i.e., add a bang to all fields.

2. Use only strict types for the fields of the constructors.

The second requirement is problematic as it rules out the use of the standard
Haskell 'Maybe', 'Either', and pair types. This library solves this problem by
providing strict variants of these types and their corresponding standard
support functions and type-class instances.

Note that this library does currently not provide fully strict lists.
They can be added if they are really required. However, in many cases one
probably wants to use unboxed or strict boxed vectors from the 'vector' library
(<http://hackage.haskell.org/package/vector>) instead of strict lists.
Moreover, instead of 'String's one probably wants to use strict 'Text' values
from the 'text' library (<http://hackage.haskell.org/package/text>).

This library comes with batteries included; i.e., mirror functions and
instances of the lazy versions in 'base'. It also includes instances for
type-classes from the 'deepseq', 'binary', and 'hashable' packages.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%doc CHANGELOG.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
