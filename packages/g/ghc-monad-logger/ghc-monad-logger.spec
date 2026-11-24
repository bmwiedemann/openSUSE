#
# spec file for package ghc-monad-logger
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pkg_name monad-logger
%bcond_with ghc_prof
Name:           ghc-%pkg_name
Version:        0.3.42
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        A class of monads which can log messages
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-loops-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-stm-chans-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unliftio-core-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-lifted-base-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-monad-loops-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-stm-chans-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-prof
%endif

%description
A class of monads which can log messages.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1 -n %pkg_name-%{version}

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
%doc ChangeLog.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
