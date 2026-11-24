#
# spec file for package ghc-http2
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


%global pkg_name http2
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        5.4.14
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        HTTP/2 library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-http-semantics-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-network-byte-order-devel
BuildRequires:  ghc-network-control-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-manager-devel
BuildRequires:  ghc-unix-time-devel
BuildRequires:  ghc-utf8-string-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-http-semantics-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-network-byte-order-prof
BuildRequires:  ghc-network-control-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-time-manager-prof
BuildRequires:  ghc-unix-time-prof
BuildRequires:  ghc-utf8-string-prof
%endif
%if %{with tests}
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-network-run-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-typed-process-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Glob-prof
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-network-run-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-typed-process-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
%endif
%endif

%description
HTTP/2 library including frames, HPACK, client and server.

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
%doc ChangeLog.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
