#
# spec file for package ghc-yaml
#
# Copyright (c) 2023 SUSE LLC
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


%global pkg_name yaml
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.11.11.2
Release:        0
Summary:        Support for parsing and rendering YAML documents
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-libyaml-devel
BuildRequires:  ghc-libyaml-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-raw-strings-qq-devel
BuildRequires:  ghc-raw-strings-qq-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-mockery-devel
BuildRequires:  ghc-mockery-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
%endif

%description
README and API documentation are available at
<https://www.stackage.org/package/yaml>.

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
%define cabal_configure_options -f-no-examples -f-no-exe
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/examples
%{_bindir}/json2yaml
%{_bindir}/yaml2json

%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
