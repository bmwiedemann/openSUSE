#
# spec file for package ghc-serialise
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


%global pkg_name serialise
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.6.0
Release:        0
Summary:        A binary serialisation library for Haskell values
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-half-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
This package (formerly 'binary-serialise-cbor') provides pure, efficient
serialization of Haskell values directly into 'ByteString's for storage or
transmission purposes. By providing a set of type class instances, you can also
serialise any custom data type you have as well.

The underlying binary format used is the 'Concise Binary Object
Representation', or CBOR, specified in RFC 7049. As a result, serialised
Haskell values have implicit structure outside of the Haskell program itself,
meaning they can be inspected or analyzed without custom tools.

An implementation of the standard bijection between CBOR and JSON is provided
by the [cborg-json](/package/cborg-json) package. Also see
[cbor-tool](/package/cbor-tool) for a convenient command-line utility for
working with CBOR data.

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
%license LICENSE.txt

%files devel -f %{name}-devel.files
%doc ChangeLog.md

%changelog
