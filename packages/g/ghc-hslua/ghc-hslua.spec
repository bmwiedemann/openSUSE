#
# spec file for package ghc-hslua
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


%global pkg_name hslua
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.2.1
Release:        0
Summary:        Bindings to Lua, an embeddable scripting language
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-hslua-aeson-devel
BuildRequires:  ghc-hslua-classes-devel
BuildRequires:  ghc-hslua-core-devel
BuildRequires:  ghc-hslua-marshalling-devel
BuildRequires:  ghc-hslua-objectorientation-devel
BuildRequires:  ghc-hslua-packaging-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-lua-arbitrary-devel
BuildRequires:  ghc-lua-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hslua-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif

%description
HsLua provides wrappers and helpers to bridge Haskell and <https://www.lua.org/
Lua>.

It builds upon the /lua/ package, which allows to bundle a Lua interpreter with
a Haskell program.

Example programs are can be found in the 'hslua-examples' subdir of the project
<https://github.com/hslua/hslua repository>.

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
%define cabal_configure_options -f-system-lua
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

%changelog
