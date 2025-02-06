#
# spec file for package ghc-psqueues
#
# Copyright (c) 2025 SUSE LLC
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


%global pkg_name psqueues
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.8.1
Release:        0
Summary:        Pure priority search queues
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
%endif

%description
The psqueues package provides <http://en.wikipedia.org/wiki/Priority_queue
Priority Search Queues> in three different flavors.

* 'OrdPSQ k p v', which uses the 'Ord k' instance to provide fast insertion,
deletion and lookup. This implementation is based on Ralf Hinze's
<http://citeseer.ist.psu.edu/hinze01simple.html A Simple Implementation
Technique for Priority Search Queues>. Hence, it is similar to the
<http://hackage.haskell.org/package/PSQueue PSQueue> library, although it is
considerably faster and provides a slightly different API.

* 'IntPSQ p v' is a far more efficient implementation. It fixes the key type to
'Int' and uses a <http://en.wikipedia.org/wiki/Radix_tree radix tree> (like
'IntMap') with an additional min-heap property.

* 'HashPSQ k p v' is a fairly straightforward extension of 'IntPSQ': it simply
uses the keys' hashes as indices in the 'IntPSQ'. If there are any hash
collisions, it uses an 'OrdPSQ' to resolve those. The performance of this
implementation is comparable to that of 'IntPSQ', but it is more widely
applicable since the keys are not restricted to 'Int', but rather to any
'Hashable' datatype.

Each of the three implementations provides the same API, so they can be used
interchangeably. The benchmarks show how they perform relative to one another,
and also compared to the other Priority Search Queue implementations on
Hackage: <http://hackage.haskell.org/package/PSQueue PSQueue> and
<http://hackage.haskell.org/package/fingertree-psqueue fingertree-psqueue>.

<<http://i.imgur.com/KmbDKR6.png>>

<<http://i.imgur.com/ClT181D.png>>

Typical applications of Priority Search Queues include:

* Caches, and more specifically LRU Caches;

* Schedulers;

* Pathfinding algorithms, such as Dijkstra's and A*.

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
%doc CHANGELOG

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
