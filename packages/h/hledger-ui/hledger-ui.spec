#
# spec file for package hledger-ui
#
# Copyright (c) 2023 SUSE LLC
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


Name:           hledger-ui
Version:        1.28
Release:        0
Summary:        Curses-style terminal interface for the hledger accounting system
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-brick-devel
BuildRequires:  ghc-brick-prof
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-cmdargs-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-fsnotify-devel
BuildRequires:  ghc-fsnotify-prof
BuildRequires:  ghc-hledger-devel
BuildRequires:  ghc-hledger-lib-devel
BuildRequires:  ghc-hledger-lib-prof
BuildRequires:  ghc-hledger-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-platform-devel
BuildRequires:  ghc-microlens-platform-prof
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-zipper-devel
BuildRequires:  ghc-text-zipper-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-vty-devel
BuildRequires:  ghc-vty-prof
ExcludeArch:    %{ix86}

%description
A simple curses-style terminal user interface for the hledger accounting
system. It can be a more convenient way to browse your accounts than the CLI.
This package currently does not support Microsoft Windows, except in WSL.

hledger is a robust, cross-platform set of tools for tracking money, time, or
any other commodity, using double-entry accounting and a simple, editable file
format, with command-line, terminal and web interfaces. It is a Haskell rewrite
of Ledger, and one of the leading implementations of Plain Text Accounting.
Read more at: <https://hledger.org>.

%prep
%autosetup

%build
%ghc_bin_build

%install
%ghc_bin_install

%files
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/%{name}

%changelog
