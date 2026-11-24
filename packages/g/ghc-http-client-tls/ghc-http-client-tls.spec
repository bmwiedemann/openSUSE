#
# spec file for package ghc-http-client-tls
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


%global pkg_name http-client-tls
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.4.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Http-client backend using the connection package and tls library
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-md5-devel
BuildRequires:  ghc-crypton-connection-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptohash-md5-prof
BuildRequires:  ghc-crypton-connection-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-transformers-prof
%endif
%if %{with tests}
BuildRequires:  ghc-hspec-devel
%if %{with ghc_prof}
BuildRequires:  ghc-hspec-prof
%endif
%endif

%description
Hackage documentation generation is not reliable. For up to date documentation,
please see: <https://www.stackage.org/package/http-client-tls>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%doc ChangeLog.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
