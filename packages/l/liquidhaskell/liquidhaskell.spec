#
# spec file for package liquidhaskell
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


%global pkg_name liquidhaskell
%bcond_with tests
Name:           %{pkg_name}
Version:        0.8.10.2
Release:        0
Summary:        Liquid Types for Haskell
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch1:         fix-build-with-diff-0.4.x-part-1.patch
Patch2:         fix-build-with-diff-0.4.x-part-2.patch
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fingertree-devel
BuildRequires:  ghc-ghc-boot-devel
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-ghc-paths-devel
BuildRequires:  ghc-githash-devel
BuildRequires:  ghc-gitrev-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hscolour-devel
BuildRequires:  ghc-liquid-fixpoint-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-optics-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-simple-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-string-conv-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tasty-ant-xml-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-rerun-devel
%endif

%description
Liquid Types for Haskell.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup -p1
cabal-tweak-dep-ver optparse-applicative '< 0.16.0.0' '< 1'

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/liquid
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/include
%dir %{_datadir}/%{name}-%{version}/include/710
%dir %{_datadir}/%{name}-%{version}/include/710/Data
%dir %{_datadir}/%{name}-%{version}/include/Control
%dir %{_datadir}/%{name}-%{version}/include/Control/Parallel
%dir %{_datadir}/%{name}-%{version}/include/Data
%dir %{_datadir}/%{name}-%{version}/include/Data/ByteString
%dir %{_datadir}/%{name}-%{version}/include/Data/Text
%dir %{_datadir}/%{name}-%{version}/include/Data/Text/Fusion
%dir %{_datadir}/%{name}-%{version}/include/Data/Text/Lazy
%dir %{_datadir}/%{name}-%{version}/include/Foreign
%dir %{_datadir}/%{name}-%{version}/include/Foreign/C
%dir %{_datadir}/%{name}-%{version}/include/Foreign/Marshal
%dir %{_datadir}/%{name}-%{version}/include/GHC
%dir %{_datadir}/%{name}-%{version}/include/GHC/IO
%dir %{_datadir}/%{name}-%{version}/include/Language
%dir %{_datadir}/%{name}-%{version}/include/Language/Haskell
%dir %{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid
%dir %{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid/Synthesize
%dir %{_datadir}/%{name}-%{version}/include/System
%dir %{_datadir}/%{name}-%{version}/mirror-modules
%dir %{_datadir}/%{name}-%{version}/mirror-modules/templates
%dir %{_datadir}/%{name}-%{version}/syntax
%{_datadir}/%{name}-%{version}/include/*.hquals
%{_datadir}/%{name}-%{version}/include/*.hs
%{_datadir}/%{name}-%{version}/include/*.hs
%{_datadir}/%{name}-%{version}/include/*.spec
%{_datadir}/%{name}-%{version}/include/710/Data/*.spec
%{_datadir}/%{name}-%{version}/include/Control/*.spec
%{_datadir}/%{name}-%{version}/include/Control/Parallel/*.spec
%{_datadir}/%{name}-%{version}/include/CoreToLogic.lg
%{_datadir}/%{name}-%{version}/include/Data/*.hquals
%{_datadir}/%{name}-%{version}/include/Data/*.spec
%{_datadir}/%{name}-%{version}/include/Data/ByteString/*.spec
%{_datadir}/%{name}-%{version}/include/Data/Text/*.spec
%{_datadir}/%{name}-%{version}/include/Data/Text/Fusion/*.spec
%{_datadir}/%{name}-%{version}/include/Data/Text/Lazy/*.spec
%{_datadir}/%{name}-%{version}/include/Foreign/*.spec
%{_datadir}/%{name}-%{version}/include/Foreign/C/*.spec
%{_datadir}/%{name}-%{version}/include/Foreign/Marshal/*.spec
%{_datadir}/%{name}-%{version}/include/GHC/*.hquals
%{_datadir}/%{name}-%{version}/include/GHC/*.spec
%{_datadir}/%{name}-%{version}/include/GHC/IO/*.spec
%{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid/*.hs
%{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid/*.hs
%{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid/*.pred
%{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid/*.pred
%{_datadir}/%{name}-%{version}/include/Language/Haskell/Liquid/Synthesize/*.hs
%{_datadir}/%{name}-%{version}/include/System/*.spec
%{_datadir}/%{name}-%{version}/mirror-modules/templates/MirrorModule.mustache
%{_datadir}/%{name}-%{version}/syntax/liquid.css

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.md README.md

%changelog
