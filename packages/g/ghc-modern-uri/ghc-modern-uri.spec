#
# spec file for package ghc-modern-uri
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name modern-uri
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.6.1
Release:        0
Summary:        Modern library for working with URIs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-reflection-devel
BuildRequires:  ghc-reflection-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-megaparsec-devel
BuildRequires:  ghc-hspec-megaparsec-prof
BuildRequires:  ghc-hspec-prof
%endif

%description
Modern library for working with URIs.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%license LICENSE.md

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE.md

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
