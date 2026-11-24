#
# spec file for package ghc-persistent
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


%global pkg_name persistent
%bcond_with ghc_prof
%bcond_with tests
Name:           ghc-%pkg_name
Version:        2.18.1.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Type-safe, multi-backend data serialization
License:        MIT
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-attoparsec-aeson-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-lift-type-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-path-pieces-devel
BuildRequires:  ghc-replace-megaparsec-devel
BuildRequires:  ghc-resource-pool-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-aeson-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-http-api-data-prof
BuildRequires:  ghc-lift-type-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-path-pieces-prof
BuildRequires:  ghc-replace-megaparsec-prof
BuildRequires:  ghc-resource-pool-prof
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-silently-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-lift-instances-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-prof
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vault-prof
BuildRequires:  ghc-vector-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-shakespeare-devel
%if %{with ghc_prof}
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-quickcheck-instances-prof
BuildRequires:  ghc-shakespeare-prof
%endif
%endif

%description
Hackage documentation generation is not reliable. For up to date documentation,
please see: <http://www.stackage.org/package/persistent>.

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
cabal-tweak-dep-ver template-haskell '<2.24' '<2.25'

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
