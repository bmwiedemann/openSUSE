#
# spec file for package ghc-citeproc
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


%global pkg_name citeproc
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.14.2
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Generates citations and bibliography from CSL styles
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-icu-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unicode-collation-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-xml-conduit-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-file-embed-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-text-icu-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unicode-collation-prof
BuildRequires:  ghc-uniplate-prof
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-prof
%endif
%if %{with tests}
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-timeit-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-timeit-prof
%endif
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
%define cabal_configure_options -fexecutable -ficu
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %pkg_name-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/%pkg_name

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
