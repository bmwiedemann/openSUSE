#
# spec file for package ghc-test-framework
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name test-framework
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8.2.0
Release:        0
Summary:        Framework for running and organising tests, with HUnit and QuickCheck support
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/6.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-hostname-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-xml-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-libxml-devel
BuildRequires:  ghc-semigroups-devel
%endif

%description
Allows tests such as QuickCheck properties and HUnit test cases to be assembled
into test groups, run in parallel (but reported in deterministic order, to aid
diff interpretation) and filtered and controlled by command line options.
All of this comes with colored test output, progress reporting and test
statistics output.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc ChangeLog.md

%changelog
