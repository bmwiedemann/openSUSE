#
# spec file for package ghc-typst
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


%global pkg_name typst
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.6.2
Release:        0
Summary:        Parsing and evaluating typst syntax
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cassava-devel
BuildRequires:  ghc-cassava-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-ordered-containers-devel
BuildRequires:  ghc-ordered-containers-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-toml-parser-devel
BuildRequires:  ghc-toml-parser-prof
BuildRequires:  ghc-typst-symbols-devel
BuildRequires:  ghc-typst-symbols-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-yaml-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-prof
%endif

%description
A library for parsing and evaluating typst syntax. Typst (<https://typst.app>)
is a document layout and formatting language. This library targets typst 0.10
and currently offers only partial support.

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
%doc CHANGELOG.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
