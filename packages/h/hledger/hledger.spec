#
# spec file for package hledger
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


%global pkg_name hledger
%bcond_with tests
Name:           %{pkg_name}
Version:        1.19.1
Release:        0
Summary:        Command-line interface for the hledger accounting system
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Decimal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-base-compat-batteries-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-hledger-lib-devel
BuildRequires:  ghc-lucid-devel
BuildRequires:  ghc-math-functions-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-tabular-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-terminfo-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-timeit-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utility-ht-devel
BuildRequires:  ghc-wizards-devel

%description
The command-line interface for the hledger accounting system. Its basic
function is to read a plain text file describing financial transactions and
produce useful reports.

hledger is a robust, cross-platform set of tools for tracking money, time, or
any other commodity, using double-entry accounting and a simple, editable file
format, with command-line, terminal and web interfaces. It is a Haskell rewrite
of Ledger, and one of the leading implementations of Plain Text Accounting.
Read more at: <https://hledger.org>.

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

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.md README.md

%changelog
