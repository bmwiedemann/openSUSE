#
# spec file for package ghc-citeproc
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


%global pkg_name citeproc
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8.1.1
Release:        0
Summary:        Generates citations and bibliography from CSL styles
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-icu-devel
BuildRequires:  ghc-text-icu-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unicode-collation-devel
BuildRequires:  ghc-unicode-collation-prof
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-uniplate-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-timeit-devel
BuildRequires:  ghc-timeit-prof
%endif

%description
Citeproc parses CSL style files and uses them to generate a list of formatted
citations and bibliography entries. For more information about CSL, see
<https://citationstyles.org/>.

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
%define cabal_configure_options -f+executable
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
%{_bindir}/citeproc

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
