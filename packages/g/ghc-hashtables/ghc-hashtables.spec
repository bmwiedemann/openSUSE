#
# spec file for package ghc-hashtables
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


%global pkg_name hashtables
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.2.4.1
Release:        0
Summary:        Mutable hash tables in the ST monad
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif

%description
This package provides a couple of different implementations of mutable hash
tables in the ST monad, as well as a typeclass abstracting their common
operations, and a set of wrappers to use the hash tables in the IO monad.

/QUICK START/: documentation for the hash table operations is provided in the
"Data.HashTable.Class" module, and the IO wrappers (which most users will
probably prefer) are located in the "Data.HashTable.IO" module.

This package currently contains three hash table implementations:

1. "Data.HashTable.ST.Cuckoo" contains an implementation of "cuckoo hashing" as
introduced by Pagh and Rodler in 2001 (see
<http://en.wikipedia.org/wiki/Cuckoo_hashing>). Cuckoo hashing has worst-case
/O(1)/ lookups and can reach a high "load factor", in which the table can
perform acceptably well even when approaching 90% full. Randomized testing
shows this implementation of cuckoo hashing to be slightly faster on insert and
slightly slower on lookup than "Data.HashTable.ST.Basic", while being more
space efficient by about a half-word per key-value mapping. Cuckoo hashing,
like the basic hash table implementation using linear probing, can suffer from
long delays when the table is resized.

2. "Data.HashTable.ST.Basic" contains a basic open-addressing hash table using
linear probing as the collision strategy. On a pure speed basis it should
currently be the fastest available Haskell hash table implementation for
lookups, although it has a higher memory overhead than the other tables and can
suffer from long delays when the table is resized because all of the elements
in the table need to be rehashed.

3. "Data.HashTable.ST.Linear" contains a linear hash table (see
<http://en.wikipedia.org/wiki/Linear_hashing>), which trades some insert and
lookup performance for higher space efficiency and much shorter delays when
expanding the table. In most cases, benchmarks show this table to be currently
slightly faster than 'Data.HashTable' from the Haskell base library.

It is recommended to create a concrete type alias in your code when using this
package, i.e.:

> import qualified Data.HashTable.IO as H > > type HashTable k v =
H.BasicHashTable k v > > foo :: IO (HashTable Int Int) > foo = do > ht <- H.new
> H.insert ht 1 1 > return ht

Firstly, this makes it easy to switch to a different hash table implementation,
and secondly, using a concrete type rather than leaving your functions abstract
in the HashTable class should allow GHC to optimize away the typeclass
dictionaries.

This package accepts a couple of different cabal flags:

* 'unsafe-tricks', default /ON/. If this flag is enabled, we use some unsafe
GHC-specific tricks to save indirections (namely 'unsafeCoerce#' and
'reallyUnsafePtrEquality#'. These techniques rely on assumptions about the
behaviour of the GHC runtime system and, although they've been tested and
should be safe under normal conditions, are slightly dangerous. Caveat emptor.
In particular, these techniques are incompatible with HPC code coverage
reports.

* 'sse42', default /OFF/. If this flag is enabled, we use some SSE 4.2
instructions (see <http://en.wikipedia.org/wiki/SSE4>, first available on Intel
Core 2 processors) to speed up cache-line searches for cuckoo hashing.

* 'bounds-checking', default /OFF/. If this flag is enabled, array accesses are
bounds-checked.

* 'debug', default /OFF/. If turned on, we'll rudely spew debug output to
stdout.

* 'portable', default /OFF/. If this flag is enabled, we use only pure Haskell
code and try not to use unportable GHC extensions. Turning this flag on forces
'unsafe-tricks' and 'sse42' /OFF/.

Please send bug reports to
<https://github.com/gregorycollins/hashtables/issues>.

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
