#
# spec file for package ghc-random
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name random
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.2.1.3
Release:        0
Summary:        Pseudo-random number generation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-splitmix-devel
BuildRequires:  ghc-splitmix-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-smallcheck-devel
BuildRequires:  ghc-smallcheck-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-inspection-testing-devel
BuildRequires:  ghc-tasty-inspection-testing-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-smallcheck-devel
BuildRequires:  ghc-tasty-smallcheck-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
%endif

%description
This package provides basic pseudo-random number generation, including the
ability to split random number generators.

== "System.Random": pure pseudo-random number interface

In pure code, use 'System.Random.uniform' and 'System.Random.uniformR' from
"System.Random" to generate pseudo-random numbers with a pure pseudo-random
number generator like 'System.Random.StdGen'.

As an example, here is how you can simulate rolls of a six-sided die using
'System.Random.uniformR':

>>> let roll = uniformR (1, 6) :: RandomGen g => g -> (Word, g) >>> let rolls =
unfoldr (Just . roll) :: RandomGen g => g -> [Word] >>> let pureGen = mkStdGen
42 >>> take 10 (rolls pureGen) :: [Word] [1,1,3,2,4,5,3,4,6,2]

See "System.Random" for more details.

== "System.Random.Stateful": monadic pseudo-random number interface

In monadic code, use 'System.Random.Stateful.uniformM' and
'System.Random.Stateful.uniformRM' from "System.Random.Stateful" to generate
pseudo-random numbers with a monadic pseudo-random number generator, or using a
monadic adapter.

As an example, here is how you can simulate rolls of a six-sided die using
'System.Random.Stateful.uniformRM':

>>> let rollM = uniformRM (1, 6) :: StatefulGen g m => g -> m Word >>> let
pureGen = mkStdGen 42 >>> runStateGen_ pureGen (replicateM 10 . rollM) ::
[Word] [1,1,3,2,4,5,3,4,6,2]

The monadic adapter 'System.Random.Stateful.runStateGen_' is used here to lift
the pure pseudo-random number generator 'pureGen' into the
'System.Random.Stateful.StatefulGen' context.

The monadic interface can also be used with existing monadic pseudo-random
number generators. In this example, we use the one provided in the
<https://hackage.haskell.org/package/mwc-random mwc-random> package:

>>> import System.Random.MWC as MWC >>> let rollM = uniformRM (1, 6) ::
StatefulGen g m => g -> m Word >>> monadicGen <- MWC.create >>> replicateM 10
(rollM monadicGen) :: IO [Word] [2,3,6,6,4,4,3,1,5,4]

See "System.Random.Stateful" for more details.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

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
%doc CHANGELOG.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
