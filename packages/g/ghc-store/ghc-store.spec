#
# spec file for package ghc-store
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


%global pkg_name store
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.5.1.2
Release:        0
Summary:        Fast binary serialization
License:        MIT
Group:          Development/Libraries/Haskell
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-cryptohash-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-smallcheck-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mono-traversable-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-smallcheck-devel
BuildRequires:  ghc-store-core-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-th-orphans-devel
BuildRequires:  ghc-th-reify-many-devel
BuildRequires:  ghc-th-utilities-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-void-devel
%if %{with tests}
BuildRequires:  ghc-clock-devel
%endif

%description
Fast binary serialization.

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
