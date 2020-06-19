#
# spec file for package ghc-http2
#
# Copyright (c) 2020 SUSE LLC
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


%global pkg_name http2
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.0.4
Release:        0
Summary:        HTTP/2 library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-network-byte-order-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-manager-devel
%if %{with tests}
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%endif

%description
HTTP/2 library including frames, priority queues, HPACK and server.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}

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
%doc ChangeLog.md

%changelog
