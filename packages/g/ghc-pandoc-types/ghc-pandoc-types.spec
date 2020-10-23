#
# spec file for package ghc-pandoc-types
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


%global pkg_name pandoc-types
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.22
Release:        0
Summary:        Types for representing a structured document
License:        GPL-2.0-only
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-string-qq-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
'Text.Pandoc.Definition' defines the 'Pandoc' data structure, which is used by
pandoc to represent structured documents. This module used to live in the
pandoc package, but starting with pandoc 1.7, it has been split off, so that
other packages can use it without drawing in all of pandoc's dependencies, and
pandoc itself can depend on packages (like citeproc-hs) that use them.

'Text.Pandoc.Builder' provides functions for building up 'Pandoc' structures
programmatically.

'Text.Pandoc.Generic' provides generic functions for manipulating Pandoc
documents.

'Text.Pandoc.Walk' provides faster, nongeneric functions for manipulating
Pandoc documents.

'Text.Pandoc.JSON' provides functions for serializing and deserializing a
'Pandoc' structure to and from JSON.

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
%doc changelog

%changelog
