#
# spec file for package ghc-statistics-linreg
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


%global pkg_name statistics-linreg
Name:           ghc-%{pkg_name}
Version:        0.3
Release:        0
Summary:        Linear regression between two samples, based on the 'statistics' package
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-MonadRandom-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-shuffle-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-statistics-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}

%description
Provides functions to perform a linear regression between 2 samples, see the
documentation of the linearRegression functions. This library is based on the
'statistics' package.

* 0.3: you can now use all functions on any instance of the Vector class (not
just unboxed vectors).

* 0.2.4: added distribution estimations for standard regression parameters.

* 0.2.3: added robust-fit support.

* 0.2.2: added the Total-Least-Squares version and made some refactoring to
eliminate code duplication

* 0.2.1: added the r-squared version and improved the performances.

Code sample:

> import qualified Data.Vector.Unboxed as U > > test :: Int -> IO () > test k =
do > let n = 10000000 > let a = k*n + 1 > let b = (k+1)*n > let xs = U.fromList
[a..b] > let ys = U.map (x -> x*100 + 2000) xs > -- thus 100 and 2000 are the
alpha and beta we want > putStrLn "linearRegression:" > print $
linearRegression xs ys

The r-squared and Total-Least-Squares versions work the same way.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
