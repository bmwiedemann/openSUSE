#
# spec file for package ghc-http-client
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


%global pkg_name http-client
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.7.13.1
Release:        0
Summary:        An HTTP client engine
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-mime-types-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-zlib-devel
%endif

%description
Hackage documentation generation is not reliable. For up to date documentation,
please see: <http://www.stackage.org/package/http-client>.

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
