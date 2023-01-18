#
# spec file for package ghc-servant
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


%global pkg_name servant
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.19.1
Release:        0
Summary:        A family of combinators for defining webservices APIs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-media-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-singleton-bool-devel
BuildRequires:  ghc-sop-core-devel
BuildRequires:  ghc-string-conversions-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-vault-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-quickcheck-instances-devel
%endif

%description
A family of combinators for defining webservices APIs and serving them

You can learn about the basics in the
<http://docs.servant.dev/en/stable/tutorial/index.html tutorial>.

<https://github.com/haskell-servant/servant/blob/master/servant/CHANGELOG.md
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

%changelog
