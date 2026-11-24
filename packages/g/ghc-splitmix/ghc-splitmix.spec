#
# spec file for package ghc-splitmix
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


%global pkg_name splitmix
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.1.3.2
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Fast Splittable PRNG
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-template-haskell-devel
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-template-haskell-prof
%endif
%endif

%description
Pure Haskell implementation of SplitMix described in

Guy L. Steele, Jr., Doug Lea, and Christine H. Flood. 2014. Fast splittable
pseudorandom number generators. In Proceedings of the 2014 ACM International
Conference on Object Oriented Programming Systems Languages & Applications
(OOPSLA '14). ACM, New York, NY, USA, 453-472. DOI:
<https://doi.org/10.1145/2660193.2660195>

The paper describes a new algorithm /SplitMix/ for /splittable/ pseudorandom
number generator that is quite fast: 9 64 bit arithmetic/logical operations per
64 bits generated.

/SplitMix/ is tested with two standard statistical test suites (DieHarder and
TestU01, this implementation only using the former) and it appears to be
adequate for "everyday" use, such as Monte Carlo algorithms and randomized data
structures where speed is important.

In particular, it __should not be used for cryptographic or security
applications__, because generated sequences of pseudorandom values are too
predictable (the mixing functions are easily inverted, and two successive
outputs suffice to reconstruct the internal state).

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

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
%autosetup -p1 -n %pkg_name-%{version}

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
%doc Changelog.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
