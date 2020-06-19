#
# spec file for package ghc-utility-ht
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


%global pkg_name utility-ht
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.0.15
Release:        0
Summary:        Various small helper functions for Lists, Maybes, Tuples, Functions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
%endif

%description
Various small helper functions for Lists, Maybes, Tuples, Functions.
Some of these functions are improved implementations of standard functions.
They have the same name as their standard counterparts. Others are equivalent
to functions from the 'base' package, but if you import them from this utility
package then you can write code that runs on older GHC versions or other
compilers like Hugs and JHC.

All modules are plain Haskell 98. The package depends exclusively on the 'base'
package and only that portions of 'base' that are simple to port. Thus you do
not risk a dependency avalanche by importing it. However, further splitting the
base package might invalidate this statement.

Alternative packages: 'Useful', 'MissingH'.

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
