#
# spec file for package ghc-crypton-connection
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


%global pkg_name crypton-connection
%global pkgver %{pkg_name}-%{version}
Name:           ghc-%{pkg_name}
Version:        0.4.3
Release:        0
Summary:        Simple and easy network connection API
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-basement-devel
BuildRequires:  ghc-basement-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-x509-devel
BuildRequires:  ghc-crypton-x509-prof
BuildRequires:  ghc-crypton-x509-store-devel
BuildRequires:  ghc-crypton-x509-store-prof
BuildRequires:  ghc-crypton-x509-system-devel
BuildRequires:  ghc-crypton-x509-system-prof
BuildRequires:  ghc-crypton-x509-validation-devel
BuildRequires:  ghc-crypton-x509-validation-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-socks-devel
BuildRequires:  ghc-socks-prof
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-prof
ExcludeArch:    %{ix86}

%description
Simple network library for all your connection needs.

Features: Really simple to use, SSL/TLS, SOCKS.

This library provides a very simple api to create sockets to a destination with
the choice of SSL/TLS, and SOCKS.

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
