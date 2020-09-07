#
# spec file for package happy
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


%bcond_with tests
Name:           happy
Version:        1.20.0
Release:        0
Summary:        Happy is a parser generator for Haskell
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  docbook-dtd
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  libxml2
BuildRequires:  libxslt
%if %{with tests}
BuildRequires:  ghc-process-devel
%endif

%description
Happy is a parser generator for Haskell. Given a grammar specification in BNF,
Happy generates Haskell code to parse the grammar. Happy works in a similar way
to the 'yacc' tool for C.

%prep
%autosetup
find . -type f -exec chmod -x {} +

%build
%ghc_bin_build
cd doc
autoreconf
# FIXME: you should use the %%configure macro
./configure
%make_build html

%install
%ghc_bin_install
install -D --mode=444 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
# drop artifacts from autoconf that differ across builds to fix build-compare
rm -rf doc/autom4te.cache doc/config.log doc/config.status

%check
%cabal_test

%files
%license LICENSE
%doc CHANGES README.md TODO doc examples
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%{_mandir}/man1/*
%{_datadir}/%{name}-%{version}/GLR_Base
%{_datadir}/%{name}-%{version}/GLR_Lib
%{_datadir}/%{name}-%{version}/GLR_Lib-ghc
%{_datadir}/%{name}-%{version}/GLR_Lib-ghc-debug
%{_datadir}/%{name}-%{version}/HappyTemplate
%{_datadir}/%{name}-%{version}/HappyTemplate-arrays
%{_datadir}/%{name}-%{version}/HappyTemplate-arrays-coerce
%{_datadir}/%{name}-%{version}/HappyTemplate-arrays-coerce-debug
%{_datadir}/%{name}-%{version}/HappyTemplate-arrays-debug
%{_datadir}/%{name}-%{version}/HappyTemplate-arrays-ghc
%{_datadir}/%{name}-%{version}/HappyTemplate-arrays-ghc-debug
%{_datadir}/%{name}-%{version}/HappyTemplate-coerce
%{_datadir}/%{name}-%{version}/HappyTemplate-ghc

%changelog
