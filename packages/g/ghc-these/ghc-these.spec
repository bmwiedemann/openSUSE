#
# spec file for package ghc-these
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


%global pkg_name these
Name:           ghc-%{pkg_name}
Version:        1.1.1.1
Release:        0
Summary:        An either-or-both data type
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-assoc-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}

%description
This package provides a data type 'These a b' which can hold a value of either
type or values of each type. This is usually thought of as an "inclusive or"
type (contrasting 'Either a b' as "exclusive or") or as an "outer join" type
(contrasting '(a, b)' as "inner join").

' data These a b = This a | That b | These a b '

Since version 1, this package was split into parts:

* <https://hackage.haskell.org/package/semialign semialign> For 'Align' and
'Zip' type-classes.

* <https://hackage.haskell.org/package/semialign-indexed semialign-indexed> For
'SemialignWithIndex' class, providing 'ialignWith' and 'izipWith'.

* <https://hackage.haskell.org/package/these-lens these-lens> For lens
combinators.

* <http://hackage.haskell.org/package/monad-chronicle monad-chronicle> For
transformers variant of 'These'.

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
%doc CHANGELOG.md

%changelog
