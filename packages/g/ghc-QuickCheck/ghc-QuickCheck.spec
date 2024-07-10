#
# spec file for package ghc-QuickCheck
#
# Copyright (c) 2023 SUSE LLC
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


%global pkg_name QuickCheck
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.14.3
Release:        0
Summary:        Automatic testing of Haskell programs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-splitmix-devel
BuildRequires:  ghc-splitmix-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
%endif

%description
QuickCheck is a library for random testing of program properties. The
programmer provides a specification of the program, in the form of properties
which functions should satisfy, and QuickCheck then tests that the properties
hold in a large number of randomly generated cases. Specifications are
expressed in Haskell, using combinators provided by QuickCheck.
QuickCheck provides combinators to define properties, observe the distribution
of test data, and define test data generators.

Most of QuickCheck's functionality is exported by the main "Test.QuickCheck"
module. The main exception is the monadic property testing library in
"Test.QuickCheck.Monadic".

If you are new to QuickCheck, you can try looking at the following resources:

* The <http://www.cse.chalmers.se/~rjmh/QuickCheck/manual.html official
QuickCheck manual>. It's a bit out-of-date in some details and doesn't cover
newer QuickCheck features, but is still full of good advice. *
<https://begriffs.com/posts/2017-01-14-design-use-quickcheck.html>, a detailed
tutorial written by a user of QuickCheck.

The <https://hackage.haskell.org/package/quickcheck-instances
quickcheck-instances> companion package provides instances for types in Haskell
Platform packages at the cost of additional dependencies.

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
%doc README changelog examples

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
