#
# spec file for package ghc-doctemplates
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


%global pkg_name doctemplates
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.11.1
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Pandoc-style document templates
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-text-conversions-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-text-conversions-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-vector-prof
%endif
%if %{with tests}
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-temporary-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-temporary-prof
%endif
%endif

%description
This is the text templating system used by pandoc. It supports variable
interpolation, iteration, tests for non-blank values, pipes, and partials.
Templates are rendered to doclayout Docs, and variable values may come from a
variety of different sources, including aeson Values.

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
%doc README.md changelog.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
