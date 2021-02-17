#
# spec file for package ghc-generic-lens-core
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name generic-lens-core
Name:           ghc-%{pkg_name}
Version:        2.1.0.0
Release:        0
Summary:        Generically derive traversals, lenses and prisms
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-indexed-profunctors-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
ExcludeArch:    %{ix86}

%description
This library uses GHC.Generics to derive efficient optics (traversals, lenses
and prisms) for algebraic data types in a type-directed way, with a focus on
good type inference and error messages when possible.

This package is the shared internal logic of the
'<https://hackage.haskell.org/package/generic-lens generic-lens>' and
'<https://hackage.haskell.org/package/generic-optics generic-optics>'
libraries.

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
%doc ChangeLog.md

%changelog
