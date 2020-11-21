#
# spec file for package ghc-brick
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


%global pkg_name brick
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.57
Release:        0
Summary:        A declarative terminal user interface library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-config-ini-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-data-clist-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-mtl-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-zipper-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vty-devel
BuildRequires:  ghc-word-wrap-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
%endif

%description
Write terminal user interfaces (TUIs) painlessly with 'brick'! You write an
event handler and a drawing function and the library does the rest.

> module Main where > > import Brick > > ui :: Widget () > ui = str "Hello,
world!" > > main :: IO () > main = simpleMain ui

To get started, see:

* <https://github.com/jtdaugherty/brick/blob/master/README.md The README>

* The <https://github.com/jtdaugherty/brick/blob/master/docs/guide.rst Brick
user guide>

* The demonstration programs in the 'programs' directory

This package deprecates <http://hackage.haskell.org/package/vty-ui vty-ui>.

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
%doc CHANGELOG.md README.md docs

%changelog
