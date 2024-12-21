#
# spec file for package ghc-pandoc-lua-engine
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


%global pkg_name pandoc-lua-engine
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.4
Release:        0
Summary:        Lua engine to power custom pandoc conversions
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-citeproc-devel
BuildRequires:  ghc-citeproc-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-doclayout-devel
BuildRequires:  ghc-doclayout-prof
BuildRequires:  ghc-doctemplates-devel
BuildRequires:  ghc-doctemplates-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hslua-devel
BuildRequires:  ghc-hslua-module-doclayout-devel
BuildRequires:  ghc-hslua-module-doclayout-prof
BuildRequires:  ghc-hslua-module-path-devel
BuildRequires:  ghc-hslua-module-path-prof
BuildRequires:  ghc-hslua-module-system-devel
BuildRequires:  ghc-hslua-module-system-prof
BuildRequires:  ghc-hslua-module-text-devel
BuildRequires:  ghc-hslua-module-text-prof
BuildRequires:  ghc-hslua-module-version-devel
BuildRequires:  ghc-hslua-module-version-prof
BuildRequires:  ghc-hslua-module-zip-devel
BuildRequires:  ghc-hslua-module-zip-prof
BuildRequires:  ghc-hslua-prof
BuildRequires:  ghc-hslua-repl-devel
BuildRequires:  ghc-hslua-repl-prof
BuildRequires:  ghc-lpeg-devel
BuildRequires:  ghc-lpeg-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pandoc-devel
BuildRequires:  ghc-pandoc-lua-marshal-devel
BuildRequires:  ghc-pandoc-lua-marshal-prof
BuildRequires:  ghc-pandoc-prof
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-lua-devel
BuildRequires:  ghc-tasty-lua-prof
BuildRequires:  ghc-tasty-prof
%endif

%description
This package provides a pandoc scripting engine based on Lua.

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
%license COPYING.md

%files devel -f %{name}-devel.files
%doc README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license COPYING.md

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
