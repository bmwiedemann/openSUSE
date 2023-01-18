#
# spec file for package ghc-hedgehog
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


%global pkg_name hedgehog
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.2
Release:        0
Summary:        Release with confidence
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-barbies-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-concurrent-output-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-erf-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-lifted-async-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-wl-pprint-annotated-devel
ExcludeArch:    %{ix86}

%description
<http://hedgehog.qa/ Hedgehog> automatically generates a comprehensive array of
test cases, exercising your software in ways human testers would never imagine.

Generate hundreds of test cases automatically, exposing even the most insidious
of corner cases. Failures are automatically simplified, giving developers
coherent, intelligible error messages.

To get started quickly, see the
<https://github.com/hedgehogqa/haskell-hedgehog/tree/master/hedgehog-example
examples>.

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
