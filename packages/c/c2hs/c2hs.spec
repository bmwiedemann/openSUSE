#
# spec file for package c2hs
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
Name:           c2hs
Version:        0.28.8
Release:        0
Summary:        C->Haskell FFI tool that gives some cross-language type safety
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/revision/3.cabal#/%{name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-language-c-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-language-c-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-shelly-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-shelly-prof
BuildRequires:  ghc-test-framework-hunit-prof
BuildRequires:  ghc-test-framework-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
%endif
%endif

%description
C->Haskell assists in the development of Haskell bindings to C libraries.
It extracts interface information from C header files and generates Haskell
code with foreign imports and marshaling. Unlike writing foreign imports by
hand (or using hsc2hs), this ensures that C functions are imported with the
correct Haskell types.

%prep
%autosetup -p1
cp -p %{SOURCE1} %{name}.cabal
chmod a-x {README,AUTHORS,ChangeLog,ChangeLog.old}

%build
%ghc_bin_build

%install
%ghc_bin_install

%check
%cabal_test

%files
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.old README doc
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/C2HS.hs

%changelog
