#
# spec file for package ghc-bitvec
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


%global pkg_name bitvec
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.1.3.0
Release:        0
Summary:        Space-efficient bit vectors
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-quickcheck-classes-base-devel
BuildRequires:  ghc-quickcheck-classes-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
A newtype over 'Bool' with a better 'Vector' instance: 8x less memory, up to
1000x faster.

The <https://hackage.haskell.org/package/vector vector> package represents
unboxed arrays of 'Bool's spending 1 byte (8 bits) per boolean. This library
provides a newtype wrapper 'Bit' and a custom instance of an unboxed 'Vector',
which packs bits densely, achieving an __8x smaller memory footprint.__ The
performance stays mostly the same; the most significant degradation happens for
random writes (up to 10% slower). On the other hand, for certain bulk bit
operations 'Vector' 'Bit' is up to 1000x faster than 'Vector' 'Bool'.

=== Thread safety

* "Data.Bit" is faster, but writes and flips are thread-unsafe. This is because
naive updates are not atomic: they read the whole word from memory, then modify
a bit, then write the whole word back. * "Data.Bit.ThreadSafe" is slower (up to
20%), but writes and flips are thread-safe.

=== Similar packages

* <https://hackage.haskell.org/package/bv bv> and
<https://hackage.haskell.org/package/bv-little bv-little> do not offer mutable
vectors.

* <https://hackage.haskell.org/package/array array> is memory-efficient for
'Bool', but lacks a handy 'Vector' interface and is not thread-safe.

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
%doc README.md changelog.md

%changelog
