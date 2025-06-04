#
# spec file for package ghc-generics-sop
#
# Copyright (c) 2025 SUSE LLC
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


%global pkg_name generics-sop
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.5.1.4
Release:        0
Summary:        Generic Programming using True Sums of Products
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-sop-core-devel
BuildRequires:  ghc-sop-core-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
ExcludeArch:    %{ix86}

%description
A library to support the definition of generic functions. Datatypes are viewed
in a uniform, structured way: the choice between constructors is represented
using an n-ary sum, and the arguments of each constructor are represented using
an n-ary product.

The module "Generics.SOP" is the main module of this library and contains more
detailed documentation.

Since version 0.4.0.0, this package is now based on
'<https://hackage.haskell.org/package/sop-core sop-core>'. The core package
contains all the functionality of n-ary sums and products, whereas this package
provides the datatype-generic programming support on top.

Examples of using this library are provided by the following packages:

* '<https://hackage.haskell.org/package/basic-sop basic-sop>' basic examples,

* '<https://hackage.haskell.org/package/pretty-sop pretty-sop>' generic pretty
printing,

* '<https://hackage.haskell.org/package/lens-sop lens-sop>' generically
computed lenses,

* '<https://hackage.haskell.org/package/json-sop json-sop>' generic JSON
conversions.

A detailed description of the ideas behind this library is provided by the
paper:

* Edsko de Vries and Andres Löh.
<http://www.andres-loeh.de/TrueSumsOfProducts True Sums of Products>.
Workshop on Generic Programming (WGP) 2014.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md doctest.sh

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
