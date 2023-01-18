#
# spec file for package ghc-microlens-ghc
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


%global pkg_name microlens-ghc
Name:           ghc-%{pkg_name}
Version:        0.4.14.1
Release:        0
Summary:        Microlens + array, bytestring, containers, transformers
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}

%description
Use this package instead of <http://hackage.haskell.org/package/microlens
microlens> if you don't mind depending on all dependencies here –
'Lens.Micro.GHC' reexports everything from 'Lens.Micro' and additionally
provides orphan instances of microlens classes for packages coming with GHC
(<http://hackage.haskell.org/package/array array>,
<http://hackage.haskell.org/package/bytestring bytestring>,
<http://hackage.haskell.org/package/containers containers>,
<http://hackage.haskell.org/package/transfromers transformers>).

The minor and major versions of microlens-ghc are incremented whenever the
minor and major versions of microlens are incremented, so you can depend on the
exact version of microlens-ghc without specifying the version of microlens you
need.

This package is a part of the <http://hackage.haskell.org/package/microlens
microlens> family; see the readme <https://github.com/monadfix/microlens#readme
on Github>.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
