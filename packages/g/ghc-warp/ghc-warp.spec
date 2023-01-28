#
# spec file for package ghc-warp
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


%global pkg_name warp
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        3.3.23
Release:        0
Summary:        A fast, light-weight web server for WAI applications
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-auto-update-devel
BuildRequires:  ghc-bsb-http-chunked-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-http-date-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http2-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-recv-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-simple-sendfile-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-manager-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-word8-devel
BuildRequires:  ghc-x509-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-process-devel
%endif

%description
HTTP/1.0, HTTP/1.1 and HTTP/2 are supported. For HTTP/2, Warp supports direct
and ALPN (in TLS) but not upgrade. API docs and the README are available at
<http://www.stackage.org/package/warp>.

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

%changelog
