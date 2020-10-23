#
# spec file for package ghc-th-compat
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


%global pkg_name th-compat
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1
Release:        0
Summary:        Backward- (and forward-)compatible Quote and Code types
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
%if %{with tests}
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-mtl-devel
%endif

%description
This package defines a "Language.Haskell.TH.Syntax.Compat" module, which
backports the 'Quote' and 'Code' types to work across a wide range of
'template-haskell' versions. On recent versions of 'template-haskell' (2.17.0.0
or later), this module simply reexports 'Quote' and 'Code' from
"Language.Haskell.TH.Syntax". Refer to the Haddocks for
"Language.Haskell.TH.Syntax.Compat" for examples of how to use this module.

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
%doc CHANGELOG.md README.md

%changelog
