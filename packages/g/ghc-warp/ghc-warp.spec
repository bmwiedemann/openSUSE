#
# spec file for package ghc-warp
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


%global pkg_name warp
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        3.4.21
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        A fast, light-weight web server for WAI applications
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-auto-update-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bsb-http-chunked-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-crypton-x509-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-http-date-devel
BuildRequires:  ghc-http-semantics-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http2-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-recv-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-simple-sendfile-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-manager-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-word8-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-auto-update-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bsb-http-chunked-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-x509-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-http-date-prof
BuildRequires:  ghc-http-semantics-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-http2-prof
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-recv-prof
BuildRequires:  ghc-simple-sendfile-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-manager-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vault-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-word8-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-process-devel
%if %{with ghc_prof}
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-process-prof
%endif
%endif

%description
HTTP/1.0, HTTP/1.1 and HTTP/2 are supported. For HTTP/2, Warp supports direct
and ALPN (in TLS) but not upgrade. API docs and the README are available at
<https://www.stackage.org/package/warp>.

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
%doc ChangeLog.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
