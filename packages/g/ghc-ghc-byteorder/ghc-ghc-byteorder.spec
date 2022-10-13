#
# spec file for package ghc-ghc-byteorder
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


%global pkg_name ghc-byteorder
Name:           ghc-%{pkg_name}
Version:        4.11.0.0.10
Release:        0
Summary:        "GHC.ByteOrder" API Compatibility Layer
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/3.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}

%description
This package transparently supplies the "GHC.ByteOrder" API as provided in
'base-4.11.0.0' for legacy GHC releases which didn't provide it yet (i.e.
GHC 7.0 through GHC 8.2).

This release reexports [GHC.ByteOrder from
base](https://hackage.haskell.org/package/base-4.11.1.0/docs/GHC-ByteOrder.html)
via Cabal's 'reexported-modules' mechanism. For GHC 8.2 and earlier a different
release of 'ghc-byteorder' (with the same minor version) is eligible by the
Cabal solver with a backported "GHC.ByteOrder" module.

In order to use this compatibility layer, simply declare a dependency on
'ghc-byteorder' in your '.cabal' package description like so

> build-depends: ghc-byteorder ^>= 4.11.0.0

And your code will be able to access this respective API version of the module
via the usual

> import GHC.ByteOrder

mechanism.

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
%ghc_lib_build_without_haddock

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
