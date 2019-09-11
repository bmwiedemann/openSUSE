#
# spec file for package ghc-pantry
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global pkg_name pantry
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.1.2
Release:        0
Summary:        Content addressable Haskell package management
License:        BSD-3-Clause
Group:          Development/Libraries/Haskell
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-cryptonite-conduit-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hpack-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-download-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mono-traversable-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-path-devel
BuildRequires:  ghc-path-io-devel
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-sqlite-devel
BuildRequires:  ghc-persistent-template-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rio-devel
BuildRequires:  ghc-rio-orphans-devel
BuildRequires:  ghc-rio-prettyprint-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-tar-conduit-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-metrics-devel
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-th-orphans-devel
BuildRequires:  ghc-th-reify-many-devel
BuildRequires:  ghc-th-utilities-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-zip-archive-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-raw-strings-qq-devel
%endif

%description
Content addressable Haskell package management.

%package devel
Summary:        Haskell %{pkg_name} library development files
Group:          Development/Libraries/Haskell
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}
echo > Setup.hs 'import Distribution.Simple'
echo >>Setup.hs 'main = defaultMain'

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
