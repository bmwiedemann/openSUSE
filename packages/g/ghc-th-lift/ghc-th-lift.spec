#
# spec file for package ghc-th-lift
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name th-lift
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8.6
Release:        0
Summary:        Derive Template Haskell's Lift class for datatypes
License:        (BSD-3-Clause OR GPL-2.0-only)
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
ExcludeArch:    %{ix86}

%description
Derive Template Haskell's 'Lift' class for datatypes using 'TemplateHaskell'.
The functionality in this package has largely been subsumed by the 'DeriveLift'
language extension, which is available in GHC 8.0 and later versions.
As such, this package is only useful as a way to backport bugfixes to
'DeriveLift' in later GHC versions back to older GHCs.

The following libraries are related:

* The <https://hackage.haskell.org/package/th-orphans th-orphans> package
provides instances for 'template-haskell' syntax types.

* The <http://hackage.haskell.org/package/th-lift-instances th-lift-instances>
package provides 'Lift' instances for types in 'base', 'text', 'bytestring',
'vector', etc. Some of these instances are only provided for old versions of
their respective libraries, as the same 'Lift' instances are also present
upstream on newer versions.

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
%license COPYING
%license BSD3
%license GPL-2

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license COPYING
%license BSD3
%license GPL-2

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
