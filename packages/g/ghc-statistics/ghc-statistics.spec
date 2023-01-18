#
# spec file for package ghc-statistics
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name statistics
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.16.1.2
Release:        0
Summary:        A library of statistical types, data, and functions
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-dense-linear-algebra-devel
BuildRequires:  ghc-math-functions-devel
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-vector-algorithms-devel
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-th-unbox-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-erf-devel
BuildRequires:  ghc-ieee754-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-expected-failure-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
This library provides a number of common functions and types useful in
statistics. We focus on high performance, numerical robustness, and use of good
algorithms. Where possible, we provide references to the statistical
literature.

The library's facilities can be divided into four broad categories:

* Working with widely used discrete and continuous probability distributions.
(There are dozens of exotic distributions in use; we focus on the most common.)

* Computing with sample data: quantile estimation, kernel density estimation,
histograms, bootstrap methods, significance testing, and regression and
autocorrelation analysis.

* Random variate generation under several different distributions.

* Common statistical tests for significant differences between samples.

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
find . -type f -exec chmod -x {} +

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
%doc README.markdown changelog.md examples

%changelog
