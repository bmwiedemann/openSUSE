#
# spec file for package ghc-http-conduit
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


%global pkg_name http-conduit
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        2.3.9.1
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        HTTP client package with conduit interface and HTTPS support
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%pkg_name-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-attoparsec-aeson-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unliftio-core-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-aeson-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-prof
%endif
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-crypton-connection-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-wai-conduit-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-tls-devel
%if %{with ghc_prof}
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-crypton-connection-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-wai-conduit-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-prof
BuildRequires:  ghc-warp-tls-prof
%endif
%endif

%description
Hackage documentation generation is not reliable. For up to date documentation,
please see: <http://www.stackage.org/package/http-conduit>.

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
cp -p %{SOURCE1} %pkg_name.cabal

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
