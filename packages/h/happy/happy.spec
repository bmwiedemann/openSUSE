#
# spec file for package happy
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
%bcond_with tests
Name:           happy
Version:        2.2
Release:        0
Summary:        Happy is a parser generator for Haskell
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-happy-lib-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
# happy reads its code templates from the data files of happy-lib at run-time.
Requires:       happy-data = %{version}
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-happy-lib-prof
%endif
%if %{with tests}
BuildRequires:  ghc-process-devel
%if %{with ghc_prof}
BuildRequires:  ghc-process-prof
%endif
%endif

%description
Happy is a parser generator for Haskell. Given a grammar specification in BNF,
Happy generates Haskell code to parse the grammar. Happy works in a similar way
to the 'yacc' tool for C.

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
%doc ChangeLog.md README.md examples
%{_bindir}/%{name}

%changelog
