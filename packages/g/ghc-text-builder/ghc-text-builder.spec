#
# spec file for package ghc-text-builder
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


%global pkg_name text-builder
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        1.0.0.5
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Efficient and flexible strict text builder
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-text-builder-core-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-text-builder-core-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-quickcheck-classes-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%if %{with ghc_prof}
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-quickcheck-classes-prof
BuildRequires:  ghc-quickcheck-instances-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-prof
%endif
%endif

%description
= Summary

Fast strict text builder and simple type-safe formatting library.

== The Builder

The builder abstraction provided by this library is much faster than the
standard lazy 'Builder' and even the recently introduced 'StrictTextBuilder'
from "text". Benchmarks are distributed with the source code. You can see the
results in the README file.

The abstraction constructs text in two phases. In the first one it estimates
the size of the byte array and in the second one it allocates it once and
populates it in one go.

== Simple and type-safe formatting library

The monoidal API of the library provides a simple yet type-safe alternative to
formatting strings via 'printf'-like tools or more involved solutions like the
popular "[formatting](https://hackage.haskell.org/package/formatting)" library.

== Quality

Every bit of the library is heavily covered with tests with CI running tests on
a variety of versions of GHC and the "text" library. This is crucial because
the "text" library has made a switch from UTF-16 to UTF-8, leading to drastic
changes in its low-level constructs, which builder libraries must rely on, and
this library supports both versions of "text".

= Ecosystem

Following is a list of libraries that, alongside this one, make an integrated
ecosystem:

- "[text-builder-time](https://hackage.haskell.org/package/text-builder-time)"
- formatters for the "time" library

- "[text-builder-core](https://hackage.haskell.org/package/text-builder-core)"
- lower-level unsafe constructs for implementing efficient formatters
compatible with this library

- "[text-builder-dev](https://hackage.haskell.org/package/text-builder-dev)" -
edge of development of new features providing a richer functionality at the
cost of more frequent major releases

-
"[text-builder-lawful-conversions](https://hackage.haskell.org/package/text-builder-lawful-conversions)"
- integration with the "lawful-conversions" library, providing bidirectional
conversions with various textual and builder types.

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
%doc CHANGELOG.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
