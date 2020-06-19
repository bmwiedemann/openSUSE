#
# spec file for package ghc-pandoc-citeproc
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


%global pkg_name pandoc-citeproc
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.17
Release:        0
Summary:        Supports using pandoc with citeproc
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HsYAML-aeson-devel
BuildRequires:  ghc-HsYAML-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hs-bibutils-devel
BuildRequires:  ghc-libyaml-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-pandoc-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rfc5051-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-setenv-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-yaml-devel
%if %{with tests}
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-temporary-devel
%endif

%description
The pandoc-citeproc library supports automatic generation of citations and a
bibliography in pandoc documents using the Citation Style Language (CSL) macro
language. More details on CSL can be found at <http://citationstyles.org/>.

In addition to a library, the package includes an executable, pandoc-citeproc,
which works as a pandoc filter and also has a mode for converting bibliographic
databases into CSL JSON and pandoc YAML metadata formats.

pandoc-citeproc originated as a fork of Andrea Rossato's citeproc-hs.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%setup -q -n %{pkg_name}-%{version}
cabal-tweak-dep-ver aeson '< 1.5' '< 2'

%build
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
%{_bindir}/%{pkg_name}
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/locales
%dir %{_datadir}/%{pkg_name}-%{version}/man
%dir %{_datadir}/%{pkg_name}-%{version}/man/man1
%{_datadir}/%{pkg_name}-%{version}/LICENSE
%{_datadir}/%{pkg_name}-%{version}/README.md
%{_datadir}/%{pkg_name}-%{version}/changelog
%{_datadir}/%{pkg_name}-%{version}/chicago-author-date.csl
%{_datadir}/%{pkg_name}-%{version}/locales/*.xml
%{_datadir}/%{pkg_name}-%{version}/man/man1/pandoc-citeproc.1

%files devel -f %{name}-devel.files

%{_mandir}/man1/pandoc-citeproc.1%{?ext_man}

%changelog
