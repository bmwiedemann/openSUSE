#
# spec file for package ghc-pandoc-lua-marshal
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


%global pkg_name pandoc-lua-marshal
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.3.0
Release:        0
Summary:        Use pandoc types in Lua
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hslua-devel
BuildRequires:  ghc-hslua-list-devel
BuildRequires:  ghc-hslua-list-prof
BuildRequires:  ghc-hslua-marshalling-devel
BuildRequires:  ghc-hslua-marshalling-prof
BuildRequires:  ghc-hslua-prof
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-lua-devel
BuildRequires:  ghc-tasty-lua-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
%endif

%description
This package provides functions to marshal and unmarshal pandoc document types
to and from Lua.

The values of most types are pushed to pandoc as "userdata" objects that wrap a
stable pointer to the Haskell value; these objects come with methods to access
and modify their properties.

Sequences are pushed as normal Lua tables, but are augmented with convenience
functions.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
