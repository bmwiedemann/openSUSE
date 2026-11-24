#
# spec file for package alex
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


%bcond_with ghc_prof
%bcond_without tests
Name:           alex
Version:        3.5.4.2
Release:        0
Summary:        Alex is a tool for generating lexical analysers in Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
%endif
%if %{with tests}
BuildRequires:  ghc-process-devel
%if %{with ghc_prof}
BuildRequires:  ghc-process-prof
%endif
%endif

%description
Alex is a tool for generating lexical analysers in Haskell. It takes a
description of tokens based on regular expressions and generates a Haskell
module containing code for scanning text efficiently. It is similar to the tool
lex or flex for C/C++.

%prep
%autosetup -p1

%build
%ghc_bin_build

%install
%ghc_bin_install

%check
%cabal_test

%files
%license LICENSE
%doc CHANGELOG.md README.md examples
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/AlexTemplate.hs
%{_datadir}/%{name}-%{version}/AlexWrappers.hs

%changelog
