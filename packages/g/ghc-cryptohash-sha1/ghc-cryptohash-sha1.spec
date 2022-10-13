#
# spec file for package ghc-cryptohash-sha1
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


%global pkg_name cryptohash-sha1
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.11.101.0
Release:        0
Summary:        Fast, pure and practical SHA-1 implementation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
A practical incremental and one-pass, pure API to the
<https://en.wikipedia.org/wiki/SHA-1 SHA-1 hash algorithm> (including
<https://en.wikipedia.org/wiki/HMAC HMAC> support) with performance close to
the fastest implementations available in other languages.

The implementation is made in C with a haskell FFI wrapper that hides the C
implementation.

NOTE: This package has been forked off 'cryptohash-0.11.7' because the
'cryptohash' package has been deprecated and so this package continues to
satisfy the need for a lightweight package providing the SHA1 hash algorithm
without any dependencies on packages other than 'base' and 'bytestring'.

Consequently, this package can be used as a drop-in replacement for
'cryptohash''s "Crypto.Hash.SHA1" module, though with a clearly smaller
footprint.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%doc changelog.md

%changelog
