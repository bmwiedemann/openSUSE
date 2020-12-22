#
# spec file for package ghc-filepattern
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


%global pkg_name filepattern
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.2
Release:        0
Summary:        File path glob-like matching
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
%endif

%description
A library for matching files using patterns such as '"src/**/*.png"' for all
'.png' files recursively under the 'src' directory. Features:

* All matching is /O(n)/. Most functions precompute some information given only
one argument.

* See "System.FilePattern" and '?==' simple matching and semantics.

* Use 'match' and 'substitute' to extract suitable strings from the '*' and
'**' matches, and substitute them back into other patterns.

* Use 'step' and 'matchMany' to perform bulk matching of many patterns against
many paths simultaneously.

* Use "System.FilePattern.Directory" to perform optimised directory traverals
using patterns.

Originally taken from the <https://hackage.haskell.org/package/shake Shake
library>.

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
