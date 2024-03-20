#
# spec file for package alex
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


%bcond_without tests
Name:           alex
Version:        3.5.1.0
Release:        0
Summary:        Alex is a tool for generating lexical analysers in Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
%endif

%description
Alex is a tool for generating lexical analysers in Haskell. It takes a
description of tokens based on regular expressions and generates a Haskell
module containing code for scanning text efficiently. It is similar to the tool
lex or flex for C/C++.

%prep
%autosetup

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
