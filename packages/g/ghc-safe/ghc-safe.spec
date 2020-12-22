#
# spec file for package ghc-safe
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


%global pkg_name safe
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.19
Release:        0
Summary:        Library of safe (exception free) functions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-deepseq-devel
%endif

%description
A library wrapping 'Prelude'/'Data.List' functions that can throw exceptions,
such as 'head' and '!!'. Each unsafe function has up to four variants, e.g.
with 'tail':

* 'tail :: [a] -> [a]', raises an error on 'tail []'.

* 'tailMay :: [a] -> /Maybe/ [a]', turns errors into 'Nothing'.

* 'tailDef :: /[a]/ -> [a] -> [a]', takes a default to return on errors.

* 'tailNote :: /String/ -> [a] -> [a]', takes an extra argument which
supplements the error message.

* 'tailSafe :: [a] -> [a]', returns some sensible default if possible, '[]' in
the case of 'tail'.

This package is divided into three modules:

* "Safe" contains safe variants of 'Prelude' and 'Data.List' functions.

* "Safe.Foldable" contains safe variants of 'Foldable' functions.

* "Safe.Exact" creates crashing versions of functions like 'zip' (errors if the
lists are not equal) and 'take' (errors if there are not enough elements), then
wraps them to provide safe variants.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGES.txt README.md

%changelog
