#
# spec file for package ghc-aws
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name aws
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.24.3
Release:        0
Summary:        Amazon Web Services (AWS) for Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-aeson-devel
BuildRequires:  ghc-attoparsec-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-byteable-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-cryptonite-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-lifted-base-prof
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-network-bsd-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-old-locale-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-conduit-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-errors-devel
BuildRequires:  ghc-errors-prof
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-quickcheck-instances-prof
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-hunit-prof
BuildRequires:  ghc-tasty-prof
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-tasty-quickcheck-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-base-prof
%endif

%description
Bindings for Amazon Web Services (AWS), with the aim of supporting all AWS
services. To see a high level overview of the library, see the README at
<https://github.com/aristidb/aws/blob/master/README.md>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

%prep
%autosetup -n %{pkg_name}-%{version}
cabal-tweak-dep-ver data-default '< 0.8' ' < 1'
cabal-tweak-dep-ver filepath '< 1.5' ' < 2'

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
%doc CHANGELOG.md README.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
