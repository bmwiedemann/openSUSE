#
# spec file for package ghc-monad-control
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


%global pkg_name monad-control
Name:           ghc-%{pkg_name}
Version:        1.0.2.3
Release:        0
Summary:        Lift control operations, like exception catching, through monad transformers
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel

%description
This package defines the type class 'MonadBaseControl', a subset of 'MonadBase'
into which generic control operations such as 'catch' can be lifted from 'IO'
or any other base monad. Instances are based on monad transformers in
'MonadTransControl', which includes all standard monad transformers in the
'transformers' library except 'ContT'.

See the <http://hackage.haskell.org/package/lifted-base lifted-base> package
which uses 'monad-control' to lift 'IO' operations from the 'base' library
(like 'catch' or 'bracket') into any monad that is an instance of 'MonadBase'
or 'MonadBaseControl'.

Note that this package is a rewrite of Anders Kaseorg's 'monad-peel' library.
The main difference is that this package provides CPS style operators and
exploits the 'RankNTypes' and 'TypeFamilies' language extensions to simplify
and speedup most definitions.

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

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG README.markdown

%changelog
