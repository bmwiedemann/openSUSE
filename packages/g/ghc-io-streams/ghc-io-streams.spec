#
# spec file for package ghc-io-streams
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


%global pkg_name io-streams
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.5.2.0
Release:        0
Summary:        Simple, composable, and easy-to-use stream I/O
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zlib-bindings-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
BuildRequires:  ghc-zlib-devel
%endif

%description
/Overview/

The io-streams library contains simple and easy-to-use primitives for I/O using
streams. Most users will want to import the top-level convenience module
"System.IO.Streams", which re-exports most of the library:

' import System.IO.Streams (InputStream, OutputStream) import qualified
System.IO.Streams as Streams '

For first-time users, 'io-streams' comes with an included tutorial, which can
be found in the "System.IO.Streams.Tutorial" module.

/Features/

The 'io-streams' user API has two basic types: 'InputStream a' and
'OutputStream a', and three fundamental I/O primitives:

' -- read an item from an input stream Streams.read :: InputStream a -> IO
(Maybe a)

-- push an item back to an input stream Streams.unRead :: a -> InputStream a ->
IO ()

-- write to an output stream Streams.write :: Maybe a -> OutputStream a -> IO
() '

Streams can be transformed by composition and hooked together with provided
combinators:

' ghci> Streams.fromList [1,2,3::Int] >>= Streams.map (*10) >>= Streams.toList
[10,20,30] '

Stream composition leaves the original stream accessible:

' ghci> input <- Streams.fromByteString "long string" ghci> wrapped <-
Streams.takeBytes 4 input ghci> Streams.read wrapped Just "long" ghci>
Streams.read wrapped Nothing ghci> Streams.read input Just " string" '

Simple types and operations in the IO monad mean straightforward and simple
exception handling and resource cleanup using Haskell standard library
facilities like 'Control.Exception.bracket'.

'io-streams' comes with:

* functions to use files, handles, concurrent channels, sockets, lists,
vectors, and more as streams.

* a variety of combinators for wrapping and transforming streams, including
compression and decompression using zlib, controlling precisely how many bytes
are read from or written to a stream, buffering output using bytestring
builders, folds, maps, filters, zips, etc.

* support for parsing from streams using 'attoparsec'.

* support for spawning processes and communicating with them using streams.

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
%doc CONTRIBUTORS README.md changelog.md

%changelog
