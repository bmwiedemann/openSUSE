#
# spec file for package ghc-split
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


%global pkg_name split
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.3.4
Release:        0
Summary:        Combinator library for splitting lists
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
%endif

%description
A collection of various methods for splitting lists into parts, akin to the
"split" function found in several mainstream languages. Here is its tale:

Once upon a time the standard "Data.List" module held no function for splitting
a list into parts according to a delimiter. Many a brave lambda-knight strove
to add such a function, but their striving was in vain, for Lo, the Supreme
Council fell to bickering amongst themselves what was to be the essential
nature of the One True Function which could cleave a list in twain (or thrain,
or any required number of parts).

And thus came to pass the split package, comprising divers functions for
splitting a list asunder, each according to its nature. And the Supreme Council
had no longer any grounds for argument, for the favored method of each was
contained therein.

To get started, see the "Data.List.Split" module.

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
%doc CHANGES README

%changelog
