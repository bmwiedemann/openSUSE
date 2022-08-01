#
# spec file for package ghc-commonmark
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name commonmark
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.2
Release:        0
Summary:        Pure Haskell commonmark parser
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unicode-data-devel
BuildRequires:  ghc-unicode-transforms-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
This library provides the core data types and functions for parsing commonmark
(<https://spec.commonmark.org>). The parser is fully commonmark-compliant and
passes the test suite. It is designed to be customizable and easily extensible.
To customize the output, create an AST, or support a new output format, one
need only define some new typeclass instances. It is also easy to add new
syntax elements or modify existing ones.

Accurate information about source positions is available for all block and
inline elements. Thus the library can be used to create an accurate syntax
highlighter or an editor with live preview.

The parser has been designed for robust performance even in pathological cases
that tend to cause stack overflows or exponential slowdowns in other parsers,
with parsing speed that varies linearly with input length.

Related packages:

- commonmark-extensions (which defines a number of syntax extensions) -
commonmark-pandoc (which allows using this parser to create a Pandoc structure)
- commonmark-cli (a command-line tool for converting and syntax-highlighting
commonmark documents).

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
%doc README.md changelog.md

%changelog
