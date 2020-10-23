#
# spec file for package hlint
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


%global pkg_name hlint
Name:           %{pkg_name}
Version:        3.2.1
Release:        0
Summary:        Source code suggestions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cpphs-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepattern-devel
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-ghc-boot-th-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-lib-parser-ex-devel
BuildRequires:  ghc-hscolour-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-refact-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel

%description
HLint gives suggestions on how to improve your source code.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}
install -D --mode=444 data/hlint.1 %{buildroot}%{_mandir}/man1/hlint.1

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc CHANGES.txt README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/HLint_QuickCheck.hs
%{_datadir}/%{name}-%{version}/HLint_TypeCheck.hs
%{_datadir}/%{name}-%{version}/Test.hs
%{_datadir}/%{name}-%{version}/default.yaml
%{_datadir}/%{name}-%{version}/hlint.1
%{_datadir}/%{name}-%{version}/hlint.ghci
%{_datadir}/%{name}-%{version}/hlint.yaml
%{_datadir}/%{name}-%{version}/hs-lint.el
%{_datadir}/%{name}-%{version}/report_template.html

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%{_mandir}/man1/hlint.1%{?ext_man}
%doc CHANGES.txt README.md

%changelog
