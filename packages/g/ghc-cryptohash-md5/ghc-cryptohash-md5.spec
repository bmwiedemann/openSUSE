#
# spec file for package ghc-cryptohash-md5
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


%global pkg_name cryptohash-md5
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.11.100.1
Release:        0
Summary:        Fast, pure and practical MD5 implementation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/5.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-pureMD5-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
A practical incremental and one-pass, pure API to the
<https://en.wikipedia.org/wiki/MD5 MD5 hash algorithm> (including
<https://en.wikipedia.org/wiki/HMAC HMAC> support) with performance close to
the fastest implementations available in other languages.

The implementation is made in C with a haskell FFI wrapper that hides the C
implementation.

If, instead, you require a pure Haskell implementation and performance is
secondary, please refer to the [pureMD5
package](https://hackage.haskell.org/package/pureMD5).

=== Packages in the 'cryptohash-*' family

- <https://hackage.haskell.org/package/cryptohash-md5 cryptohash-md5> -
<https://hackage.haskell.org/package/cryptohash-sha1 cryptohash-sha1> -
<https://hackage.haskell.org/package/cryptohash-sha256 cryptohash-sha256> -
<https://hackage.haskell.org/package/cryptohash-sha512 cryptohash-sha512>

=== Relationship to the 'cryptohash' package and its API

This package has been originally a fork of 'cryptohash-0.11.7' because the
'cryptohash' package had been deprecated and so this package continues to
satisfy the need for a lightweight package providing the MD5 hash algorithm
without any dependencies on packages other than 'base' and 'bytestring'.
The API exposed by 'cryptohash-md5-0.11.*''s "Crypto.Hash.MD5" module is
guaranteed to remain a compatible superset of the API provided by the
'cryptohash-0.11.7''s module of the same name.

Consequently, this package is designed to be used as a drop-in replacement for
'cryptohash-0.11.7''s "Crypto.Hash.MD5" module, though with a [clearly smaller
footprint by almost 3 orders of
magnitude](https://www.reddit.com/r/haskell/comments/5lxv75/psa_please_use_unique_module_names_when_uploading/dbzegx3/).

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}
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
%doc changelog.md

%changelog
