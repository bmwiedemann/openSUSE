#
# spec file for package ghc-cryptohash
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


%global pkg_name cryptohash
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.11.9
Release:        0
Summary:        Collection of crypto hashes, fast, pure and practical
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
DEPRECATED: this library is still fully functional, but please use cryptonite
for new projects and convert old one to use cryptonite. This is where things
are at nowadays.

A collection of crypto hashes, with a practical incremental and one-pass, pure
APIs, with performance close to the fastest implementations available in other
languages.

The implementations are made in C with a haskell FFI wrapper that hide the C
implementation.

Simple examples using the unified API:

> import Crypto.Hash > > sha1 :: ByteString -> Digest SHA1 > sha1 = hash > >
hexSha3_512 :: ByteString -> String > hexSha3_512 bs = show (hash bs :: Digest
SHA3_512)

Simple examples using the module API:

> import qualified Crypto.Hash.SHA1 as SHA1 > > main = putStrLn $ show $
SHA1.hash (Data.ByteString.pack [0..255])

> import qualified Crypto.Hash.SHA3 as SHA3 > > main = putStrLn $ show $ digest
> where digest = SHA3.finalize ctx > ctx = foldl' SHA3.update iCtx (map
Data.ByteString.pack [ [1,2,3], [4,5,6] ] > iCtx = SHA3.init 224.

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
%doc README.md

%changelog
