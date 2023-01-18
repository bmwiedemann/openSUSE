#
# spec file for package ghc-servant-server
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name servant-server
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.19.2
Release:        0
Summary:        A family of combinators for defining webservices APIs and serving them
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-media-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-servant-devel
BuildRequires:  ghc-sop-core-devel
BuildRequires:  ghc-string-conversions-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-wai-app-static-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-word8-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-wai-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-should-not-typecheck-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-wai-extra-devel
%endif

%description
A family of combinators for defining webservices APIs and serving them

You can learn about the basics in the
<http://docs.servant.dev/en/stable/tutorial/index.html tutorial>.

<https://github.com/haskell-servant/servant/blob/master/servant-server/example/greet.hs
Here> is a runnable example, with comments, that defines a dummy API and
implements a webserver that serves this API, using this package.

<https://github.com/haskell-servant/servant/blob/master/servant-server/CHANGELOG.md
CHANGELOG>.

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

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/greet

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
