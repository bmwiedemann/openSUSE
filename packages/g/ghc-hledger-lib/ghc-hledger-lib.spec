#
# spec file for package ghc-hledger-lib
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


%global pkg_name hledger-lib
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.19.1
Release:        0
Summary:        A reusable library providing the core functionality of hledger
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Decimal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-compat-batteries-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-cassava-devel
BuildRequires:  ghc-cassava-megaparsec-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-fgl-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashtables-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-tabular-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-timeit-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uglymemo-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
%if %{with tests}
BuildRequires:  ghc-doctest-devel
%endif

%description
A reusable library containing hledger's core functionality. This is used by
most hledger* packages so that they support the same common file formats,
command line options, reports etc.

hledger is a robust, cross-platform set of tools for tracking money, time, or
any other commodity, using double-entry accounting and a simple, editable file
format, with command-line, terminal and web interfaces. It is a Haskell rewrite
of Ledger, and one of the leading implementations of Plain Text Accounting.
Read more at: <https://hledger.org>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
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

%files devel -f %{name}-devel.files
%doc CHANGES.md README.md

%changelog
