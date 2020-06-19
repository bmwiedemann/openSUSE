#
# spec file for package ghc-aws
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


%global pkg_name aws
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.22
Release:        0
Summary:        Amazon Web Services (AWS) for Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-bsd-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-xml-conduit-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-errors-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-quickcheck-instances-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-transformers-base-devel
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

%prep
%setup -q -n %{pkg_name}-%{version}
cabal-tweak-dep-ver base64-bytestring '== 1.0.*' '< 2'

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

%changelog
