#
# spec file for package ghc-aeson
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pkg_name aeson
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        2.2.5.1
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Fast JSON parsing and encoding
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-OneTuple-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-character-ps-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-fix-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-integer-conversion-devel
BuildRequires:  ghc-integer-logarithms-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-iso8601-devel
BuildRequires:  ghc-text-short-devel
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-time-compat-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-uuid-types-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-witherable-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-OneTuple-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-character-ps-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-fix-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-integer-conversion-prof
BuildRequires:  ghc-integer-logarithms-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-strict-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-iso8601-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-short-prof
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-time-compat-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uuid-types-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-witherable-prof
%endif
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-generically-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-generic-deriving-prof
BuildRequires:  ghc-generically-prof
BuildRequires:  ghc-quickcheck-instances-prof
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-prof
%endif
%endif

%description
A JSON parsing and encoding library optimized for ease of use and high
performance.

To get started, see the documentation for the 'Data.Aeson' module below.

(A note on naming: in Greek mythology, Aeson was the father of Jason.).

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1 -n %pkg_name-%{version}

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
%doc README.markdown changelog.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
