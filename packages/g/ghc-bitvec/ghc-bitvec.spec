#
# spec file for package ghc-bitvec
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


%global pkg_name bitvec
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.1.5.0
Release:        0
Summary:        Space-efficient bit vectors
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/2.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-quickcheck-classes-base-devel
BuildRequires:  ghc-quickcheck-classes-base-prof
BuildRequires:  ghc-quickcheck-classes-devel
BuildRequires:  ghc-quickcheck-classes-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
%endif

%description
A newtype over 'Bool' with a better 'Vector' instance: 8x less memory, up to
3500x faster.

The <https://hackage.haskell.org/package/vector vector> package represents
unboxed arrays of 'Bool's spending 1 byte (8 bits) per boolean. This library
provides a newtype wrapper 'Bit' and a custom instance of an unboxed 'Vector',
which packs bits densely, achieving an __8x smaller memory footprint.__ The
performance stays mostly the same; the most significant degradation happens for
random writes (up to 10% slower). On the other hand, for certain bulk bit
operations 'Vector' 'Bit' is up to 3500x faster than 'Vector' 'Bool'.

=== Thread safety

* "Data.Bit" is faster, but writes and flips are not thread-safe. This is
because naive updates are not atomic: they read the whole word from memory,
then modify a bit, then write the whole word back. Concurrently modifying
non-intersecting slices of the same underlying array may also lead to
unexpected results, since they can share a word in memory. *
"Data.Bit.ThreadSafe" is slower (usually 10-20%), but writes and flips are
thread-safe. Additionally, concurrently modifying non-intersecting slices of
the same underlying array works as expected. However, operations that affect
multiple elements are not guaranteed to be atomic.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

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

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
