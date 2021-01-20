#
# spec file for package ghc-uniplate
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name uniplate
Name:           ghc-%{pkg_name}
Version:        1.6.13
Release:        0
Summary:        Help writing simple, concise and fast generic operations
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-unordered-containers-devel
ExcludeArch:    %{ix86}

%description
Uniplate is library for writing simple and concise generic operations.
Uniplate has similar goals to the original Scrap Your Boilerplate work, but is
substantially simpler and faster.

To get started with Uniplate you should import one of the three following
modules:

* "Data.Generics.Uniplate.Data" - to quickly start writing generic functions.
Most users should start by importing this module.

* "Data.Generics.Uniplate.Direct" - a replacement for
"Data.Generics.Uniplate.Data" with substantially higher performance (around 5
times), but requires writing instance declarations.

* "Data.Generics.Uniplate.Operations" - definitions of all the operations
defined by Uniplate. Both the above two modules re-export this module.

In addition, some users may want to make use of the following modules:

* "Data.Generics.Uniplate.Zipper" - a zipper built on top of Uniplate
instances.

* "Data.Generics.SYB" - users transitioning from the Scrap Your Boilerplate
library.

* "Data.Generics.Compos" - users transitioning from the Compos library.

* "Data.Generics.Uniplate.DataOnly" - users making use of both 'Data' and
'Direct' to avoid getting instance conflicts.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGES.txt README.md

%changelog
