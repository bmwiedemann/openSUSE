#
# spec file for package ghc-tls
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


%global pkg_name tls
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        2.6.4
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        TLS protocol native implementation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-crypton-asn1-encoding-devel
BuildRequires:  ghc-crypton-asn1-types-devel
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-x509-devel
BuildRequires:  ghc-crypton-x509-store-devel
BuildRequires:  ghc-crypton-x509-validation-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-ech-config-devel
BuildRequires:  ghc-hpke-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-ram-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-time-devel
BuildRequires:  ghc-zlib-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-crypton-asn1-encoding-prof
BuildRequires:  ghc-crypton-asn1-types-prof
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-crypton-x509-prof
BuildRequires:  ghc-crypton-x509-store-prof
BuildRequires:  ghc-crypton-x509-validation-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-ech-config-prof
BuildRequires:  ghc-hpke-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-ram-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-serialise-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-time-prof
BuildRequires:  ghc-zlib-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-time-hourglass-devel
%if %{with ghc_prof}
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-time-hourglass-prof
%endif
%endif

%description
Native Haskell TLS 1.2/1.3 protocol implementation for servers and clients.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
