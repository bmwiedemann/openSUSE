#
# spec file for package shake
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


%global pkg_name shake
%bcond_with tests
Name:           %{pkg_name}
Version:        0.19.4
Release:        0
Summary:        Build system library, like Make, but more accurate dependencies
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepattern-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-heaps-devel
BuildRequires:  ghc-js-dgtable-devel
BuildRequires:  ghc-js-flot-devel
BuildRequires:  ghc-js-jquery-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
%endif

%description
Shake is a Haskell library for writing build systems - designed as a
replacement for 'make'. See "Development.Shake" for an introduction, including
an example. The homepage contains links to a user manual, an academic paper and
further information: <https://shakebuild.com>

To use Shake the user writes a Haskell program that imports
"Development.Shake", defines some build rules, and calls the
'Development.Shake.shakeArgs' function. Thanks to do notation and infix
operators, a simple Shake build system is not too dissimilar from a simple
Makefile. However, as build systems get more complex, Shake is able to take
advantage of the excellent abstraction facilities offered by Haskell and easily
support much larger projects. The Shake library provides all the standard
features available in other build systems, including automatic parallelism and
minimal rebuilds. Shake also provides more accurate dependency tracking,
including seamless support for generated files, and dependencies on system
information (e.g. compiler version).

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
rm -Rf %{buildroot}/%{_datadir}/%{name}-%{version}/docs

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc CHANGES.txt README.md docs
%{_bindir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/html
%{_datadir}/%{name}-%{version}/html/profile.html
%{_datadir}/%{name}-%{version}/html/progress.html
%{_datadir}/%{name}-%{version}/html/shake.js

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.txt README.md

%changelog
