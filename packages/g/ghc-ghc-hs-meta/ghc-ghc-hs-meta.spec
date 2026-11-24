#
# spec file for package ghc-ghc-hs-meta
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


%global pkg_name ghc-hs-meta
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.1.5.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Translate Haskell source to Template Haskell expression
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
Patch01:        https://github.com/zacwood9/ghc-hs-meta/commit/5cf5705f3e47da79fb5580ec63c00d125cf4554a.patch#/support-ghc-9.14.patch
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-template-haskell-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-ghc-boot-prof
BuildRequires:  ghc-ghc-prof
BuildRequires:  ghc-template-haskell-prof
%endif
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%if %{with ghc_prof}
BuildRequires:  ghc-hspec-prof
%endif
%endif

%description
Translate from Haskell source code to Template Haskell expressions using the
GHC parser.

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
%license LICENSE-PyF

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE
%license LICENSE-PyF

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
