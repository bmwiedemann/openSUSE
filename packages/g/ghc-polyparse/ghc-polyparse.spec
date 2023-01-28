#
# spec file for package ghc-polyparse
#
# Copyright (c) 2023 SUSE LLC
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


%global pkg_name polyparse
Name:           ghc-%{pkg_name}
Version:        1.13
Release:        0
Summary:        A variety of alternative parser combinator libraries
License:        LGPL-2.1-only
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/6.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
ExcludeArch:    %{ix86}

%description
This version, 1.13 is a Non-Maintainer Upload (NMU). Report issues to the
Hackage Trustees issue tracker.

A variety of alternative parser combinator libraries, including the original
HuttonMeijer set. The Poly sets have features like good error reporting,
arbitrary token type, running state, lazy parsing, and so on. Finally,
Text.Parse is a proposed replacement for the standard Read class, for better
deserialisation of Haskell values from Strings.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license COPYRIGHT
%license LICENCE-LGPL
%license LICENCE-commercial

%files devel -f %{name}-devel.files
%doc Changelog.md

%changelog
