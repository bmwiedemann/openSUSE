#
# spec file for package ghc-moo
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


%global pkg_name moo
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.2
Release:        0
Summary:        Genetic algorithm library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-MonadRandom-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-gray-code-devel
BuildRequires:  ghc-mersenne-random-pure64-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-shuffle-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
%endif

%description
Moo library provides building blocks to build custom genetic algorithms in
Haskell. They can be used to find solutions to optimization and search
problems.

Variants supported out of the box: binary (using bit-strings) and continuous
(real-coded). Potentially supported variants: permutation, tree, hybrid
encodings (require customizations).

Binary GAs: binary and Gray encoding; point mutation; one-point, two-point, and
uniform crossover. Continuous GAs: Gaussian mutation; BLX-α, UNDX, and SBX
crossover. Selection operators: roulette, tournament, and stochastic universal
sampling (SUS); with optional niching, ranking, and scaling.
Replacement strategies: generational with elitism and steady state.
Constrained optimization: random constrained initialization, death penalty,
constrained selection without a penalty function. Multi-objective optimization:
NSGA-II and constrained NSGA-II.

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
%doc README.md examples

%changelog
