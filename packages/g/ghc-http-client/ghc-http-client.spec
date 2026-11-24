#
# spec file for package ghc-http-client
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


%global pkg_name http-client
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        0.7.19
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        An HTTP client engine
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
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
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-mime-types-prof
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
%endif
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-zlib-devel
%if %{with ghc_prof}
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-zlib-prof
%endif
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
