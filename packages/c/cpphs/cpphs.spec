#
# spec file for package cpphs
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


%global pkg_name cpphs
Name:           %{pkg_name}
Version:        1.20.9.1
Release:        0
Summary:        A liberalised re-implementation of cpp, the C pre-processor
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/revision/1.cabal#/%{name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-polyparse-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
ExcludeArch:    %{ix86}

%description
Cpphs is a re-implementation of the C pre-processor that is both more
compatible with Haskell, and itself written in Haskell so that it can be
distributed with compilers.

This version of the C pre-processor is pretty-much feature-complete and
compatible with traditional (K&R) pre-processors. Additional features include:
a plain-text mode; an option to unlit literate code files; and an option to
turn off macro-expansion.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
License:        LGPL-2.1-only

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
License:        LGPL-2.1-only
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup
cp -p %{SOURCE1} %{name}.cabal
find . -type f -exec chmod -x {} +

%build
%ghc_lib_build

%install
%ghc_lib_install

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENCE-LGPL
%doc CHANGELOG LICENCE-GPL LICENCE-commercial README docs
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENCE-LGPL

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGELOG LICENCE-GPL LICENCE-commercial README docs

%changelog
