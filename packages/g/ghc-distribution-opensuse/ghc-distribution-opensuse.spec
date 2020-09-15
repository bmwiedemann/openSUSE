#
# spec file for package ghc-distribution-opensuse
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


%global pkg_name distribution-opensuse
Name:           ghc-%{pkg_name}
Version:        1.1.1
Release:        0
Summary:        Types, functions, and tools to manipulate the openSUSE distribution
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hsemail-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-class-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-turtle-devel
BuildRequires:  pandoc

%description
This library is a loose collection of types, functions, and tools that users
and developers of the <https://opensuse.org/ openSUSE Linux distribution> might
find useful.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%package -n guess-changelog
Summary:        Guess changes between package versions from their changelog

%description -n guess-changelog
Given two versions of a package, this utility will find the changelog file in
each respective version, determine the changes, and write an appropriate
change log entry to stdout that can be used in an openSUSE *.changes file to
describe the update.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build
pandoc -s -t man -o guess-changelog.1 guess-changelog.md

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}
install -D -m 644 guess-changelog.1 %{buildroot}%{_mandir}/man1/guess-changelog.1

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files -n guess-changelog
%{_bindir}/guess-changelog
%{_mandir}/man1/guess-changelog.1%{?ext_man}

%files devel -f %{name}-devel.files

%changelog
