#
# spec file for package alex
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


# Disable tests on aarch64. See: https://github.com/simonmar/alex/issues/130
%ifarch aarch64
%bcond_with tests
%else
%bcond_without tests
%endif
Name:           alex
Version:        3.2.5
Release:        0
Summary:        Alex is a tool for generating lexical analysers in Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-process-devel
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
cd doc
test -f configure || autoreconf
# FIXME: you should use the %%configure macro
./configure

%install
%ghc_bin_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp doc/alex.1 %{buildroot}/%{_mandir}/man1
rm -f doc/autom4te.cache/requests doc/config.log # varies across builds, breaking build-compare

%check
# Ensure that the test suite can find the alex binary.
export PATH="%{buildroot}%{_bindir}:$PATH"
%cabal_test

%files
%license LICENSE
%doc CHANGELOG.md README.md TODO doc examples
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/AlexTemplate
%{_datadir}/%{name}-%{version}/AlexTemplate-debug
%{_datadir}/%{name}-%{version}/AlexTemplate-ghc
%{_datadir}/%{name}-%{version}/AlexTemplate-ghc-debug
%{_datadir}/%{name}-%{version}/AlexTemplate-ghc-nopred
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/*
%{_datadir}/%{name}-%{version}/AlexWrapper-basic
%{_datadir}/%{name}-%{version}/AlexWrapper-basic-bytestring
%{_datadir}/%{name}-%{version}/AlexWrapper-gscan
%{_datadir}/%{name}-%{version}/AlexWrapper-monad
%{_datadir}/%{name}-%{version}/AlexWrapper-monad-bytestring
%{_datadir}/%{name}-%{version}/AlexWrapper-monadUserState
%{_datadir}/%{name}-%{version}/AlexWrapper-monadUserState-bytestring
%{_datadir}/%{name}-%{version}/AlexWrapper-posn
%{_datadir}/%{name}-%{version}/AlexWrapper-posn-bytestring
%{_datadir}/%{name}-%{version}/AlexWrapper-strict-bytestring

%changelog
