#
# spec file for package cabal-install
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pkg_name cabal-install
%bcond_with ghc_prof
%bcond_with tests
Name:           %pkg_name
Version:        3.16.0.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        The command-line interface for Cabal and Hackage
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/revision/5.cabal#/%{name}.cabal
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-syntax-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cabal-install-solver-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-echo-devel
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-open-browser-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-resolv-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-semaphore-compat-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zlib-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-Cabal-syntax-prof
BuildRequires:  ghc-HTTP-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cabal-install-solver-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptohash-sha256-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-echo-prof
BuildRequires:  ghc-edit-distance-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hackage-security-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-open-browser-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-regex-base-prof
BuildRequires:  ghc-regex-posix-prof
BuildRequires:  ghc-resolv-prof
BuildRequires:  ghc-safe-exceptions-prof
BuildRequires:  ghc-semaphore-compat-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tar-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-zlib-prof
%endif
%if %{with tests}
BuildRequires:  ghc-Cabal-QuickCheck-devel
BuildRequires:  ghc-Cabal-described-devel
BuildRequires:  ghc-Cabal-tests-devel
BuildRequires:  ghc-Cabal-tree-diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-expected-failure-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tree-diff-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Cabal-QuickCheck-prof
BuildRequires:  ghc-Cabal-described-prof
BuildRequires:  ghc-Cabal-tests-prof
BuildRequires:  ghc-Cabal-tree-diff-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-silently-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-tasty-expected-failure-prof
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-prof
BuildRequires:  ghc-tree-diff-prof
%endif
%endif

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.

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

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1
cp -p %{SOURCE1} %{name}.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %pkg_name-%{version}
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}%{_bindir}/cabal man --raw >%{buildroot}%{_mandir}/man1/cabal.1

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc ChangeLog.md README.md
%{_bindir}/cabal
%{_mandir}/man1/cabal.1%{?ext_man}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc ChangeLog.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
