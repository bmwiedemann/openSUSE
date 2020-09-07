#
# spec file for package shelltestrunner
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


Name:           shelltestrunner
Version:        1.9
Release:        0
Summary:        Easy, repeatable testing of CLI programs/commands
License:        GPL-1.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filemanip-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-utf8-string-devel

%description
Shelltestrunner (executable: shelltest) is a portable command-line tool for
testing command-line programs, or general shell commands, released under
GPLv3+. It reads simple test specifications defining a command to run, some
input, and the expected output, stderr, and exit status. It can run tests in
parallel, selectively, with a timeout, in color, etc.

%prep
%autosetup

%build
%ghc_bin_build

%install
%ghc_bin_install

%files
%license LICENSE
%doc CHANGES README.md
%{_bindir}/shelltest

%changelog
