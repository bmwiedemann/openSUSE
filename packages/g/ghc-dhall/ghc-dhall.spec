#
# spec file for package ghc-dhall
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


%global pkg_name dhall
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.34.0
Release:        0
Summary:        A configuration language guaranteed to terminate
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-atomic-write-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-cborg-json-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-fix-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dotgen-devel
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-half-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-lens-family-core-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-parsers-devel
BuildRequires:  ghc-pretty-simple-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-repline-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-manipulate-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-uri-encode-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-generic-random-devel
BuildRequires:  ghc-mockery-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-special-values-devel
BuildRequires:  ghc-spoon-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-expected-failure-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-turtle-devel
%endif

%description
Dhall is an explicitly typed configuration language that is not Turing
complete. Despite being Turing incomplete, Dhall is a real programming language
with a type-checker and evaluator.

Use this library to parse, type-check, evaluate, and pretty-print the Dhall
configuration language. This package also includes an executable which
type-checks a Dhall file and reduces the file to a fully evaluated normal form.

Read "Dhall.Tutorial" to learn how to use this library.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%dir %{_datadir}/%{pkg_name}-%{version}/man
%{_datadir}/%{pkg_name}-%{version}/man/dhall.1

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
