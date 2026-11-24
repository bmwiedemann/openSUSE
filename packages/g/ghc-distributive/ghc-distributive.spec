#
# spec file for package ghc-distributive
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


%global pkg_name distributive
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.6.3
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Distributive functors -- Dual to Traversable
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-transformers-prof
%endif
%if %{with tests}
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-hspec-devel
%if %{with ghc_prof}
BuildRequires:  ghc-generic-deriving-prof
BuildRequires:  ghc-hspec-prof
%endif
%endif

%description
Distributive functors -- Dual to 'Traversable'.

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
%doc CHANGELOG.markdown README.markdown

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
